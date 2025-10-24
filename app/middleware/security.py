from fastapi import HTTPException, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from typing import Callable
from app.core.interfaces.security import SecurityService, RateLimiter, SecurityLogger, URLValidator
from app.core.services.security_services import InMemoryRateLimiter, FileSecurityLogger, SSRFURLValidator

class SecurityMiddleware(BaseHTTPMiddleware, SecurityService):
    """
    Middleware que implementa múltiples protecciones de seguridad:
    - A01:2021 - Broken Access Control: Headers de seguridad
    - A03:2021 - Injection: Validación de entrada
    - A05:2021 - Security Misconfiguration: Headers de seguridad
    - A07:2021 - Identification and Authentication Failures: Rate limiting
    - A09:2021 - Security Logging and Monitoring: Logging detallado
    - A10:2021 - Server-Side Request Forgery: Validación de URLs
    
    Sigue Clean Architecture y principios SOLID:
    - Single Responsibility: Cada servicio tiene una única responsabilidad
    - Open/Closed: Extensible a través de nuevas implementaciones de interfaces
    - Liskov Substitution: Servicios intercambiables que implementan las mismas interfaces
    - Interface Segregation: Interfaces específicas para cada tipo de servicio
    - Dependency Inversion: Depende de abstracciones, no implementaciones
    """
    
    def __init__(
        self,
        app,
        rate_limiter: RateLimiter = None,
        security_logger: SecurityLogger = None,
        url_validator: URLValidator = None
    ):
        super().__init__(app)
        self.rate_limiter = rate_limiter or InMemoryRateLimiter()
        self.security_logger = security_logger or FileSecurityLogger()
        self.url_validator = url_validator or SSRFURLValidator()
        
        # Headers de seguridad predefinidos
        self.security_headers = {
            'X-Content-Type-Options': 'nosniff',
            'X-Frame-Options': 'DENY',
            'X-XSS-Protection': '1; mode=block',
            'Strict-Transport-Security': 'max-age=31536000; includeSubDomains',
            #'Content-Security-Policy': "default-src 'self'", # al activarlo, solo admite archivos alojados en el mismo servidor.
            'Referrer-Policy': 'strict-origin-when-cross-origin',
            'Cache-Control': 'no-store, no-cache, must-revalidate, proxy-revalidate',
            'Pragma': 'no-cache',
            'Expires': '0',
            'X-Permitted-Cross-Domain-Policies': 'none',
            'Cross-Origin-Embedder-Policy': 'require-corp',
            'Cross-Origin-Opener-Policy': 'same-origin',
            'Cross-Origin-Resource-Policy': 'same-origin',
        }
        
    def validate_request(self, request: Request) -> None:
        """
        Valida una solicitud contra amenazas de seguridad
        
        Args:
            request (Request): Solicitud a validar
            
        Raises:
            HTTPException: Si la solicitud viola alguna política de seguridad
        """
            
        # Validar rate limiting
        client_ip = request.client.host
        if not self.rate_limiter.check_rate_limit(client_ip):
            self.security_logger.log_violation(
                "rate_limit_exceeded",
                {"client_ip": client_ip}
            )
            raise HTTPException(
                status_code=429,
                detail="Too many requests"
            )
        
        # Validar path contra inyecciones
        path = request.url.path
        if any(pattern in path.lower() for pattern in ['<', '>', 'javascript:', 'data:']):
            self.security_logger.log_violation(
                "injection_attempt",
                {"path": path}
            )
            raise HTTPException(
                status_code=400,
                detail="Invalid characters in request"
            )
            
        # Validar URLs en query params
        for param, value in request.query_params.items():
            if isinstance(value, str) and 'http' in value.lower():
                self.url_validator.validate_url(value)
    
    def enhance_response(self, response: Response) -> Response:
        """
        Mejora una respuesta con headers de seguridad
        
        Args:
            response (Response): Respuesta a mejorar
            
        Returns:
            Response: Respuesta mejorada con headers de seguridad
        """
        for header, value in self.security_headers.items():
            response.headers[header] = value
        return response
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        """
        Procesa una solicitud aplicando todas las medidas de seguridad
        
        Args:
            request (Request): Solicitud a procesar
            call_next (Callable): Función para procesar la siguiente middleware
            
        Returns:
            Response: Respuesta procesada con medidas de seguridad
            
        Raises:
            HTTPException: Si la solicitud viola alguna política de seguridad
        """
        import time
        
        try:
            start_time = time.time()
            
            # Log de inicio de solicitud
            self.security_logger.log_event(
                "request_start",
                {
                    "client_ip": request.client.host,
                    "method": request.method,
                    "path": request.url.path
                }
            )
            
            # Validar la solicitud
            self.validate_request(request)
            
            # Registrar la solicitud para rate limiting
            self.rate_limiter.register_request(request.client.host)
            
            # Procesar la solicitud
            response = await call_next(request)
            
            # Mejorar la respuesta con headers de seguridad
            response = self.enhance_response(response)
            
            # Log de finalización exitosa
            self.security_logger.log_event(
                "request_end",
                {
                    "client_ip": request.client.host,
                    "method": request.method,
                    "path": request.url.path,
                    "status_code": response.status_code,
                    "duration": time.time() - start_time
                }
            )
            
            return response
            
        except Exception as e:
            # Log de error
            self.security_logger.log_event(
                "request_error",
                {
                    "client_ip": request.client.host,
                    "method": request.method,
                    "path": request.url.path,
                    "error": str(e),
                    "error_type": type(e).__name__
                },
                level="ERROR"
            )
            raise

