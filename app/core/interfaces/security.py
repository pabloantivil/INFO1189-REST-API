from abc import ABC, abstractmethod
from typing import Dict, Any
from fastapi import Request, Response

class SecurityService(ABC):
    """Interface base para servicios de seguridad"""
    
    @abstractmethod
    def validate_request(self, request: Request) -> None:
        """Valida una solicitud"""
        pass
    
    @abstractmethod
    def enhance_response(self, response: Response) -> Response:
        """Mejora una respuesta con medidas de seguridad"""
        pass

class RateLimiter(ABC):
    """Interface para rate limiting"""
    
    @abstractmethod
    def check_rate_limit(self, client_ip: str) -> bool:
        """Verifica si una IP ha excedido el rate limit"""
        pass
    
    @abstractmethod
    def register_request(self, client_ip: str) -> None:
        """Registra una nueva solicitud"""
        pass

class SecurityLogger(ABC):
    """Interface para logging de seguridad"""
    
    @abstractmethod
    def log_event(self, event_type: str, data: Dict[str, Any], level: str = "INFO") -> None:
        """Registra un evento de seguridad"""
        pass
    
    @abstractmethod
    def log_violation(self, violation_type: str, data: Dict[str, Any]) -> None:
        """Registra una violación de seguridad"""
        pass

class URLValidator(ABC):
    """Interface para validación de URLs"""
    
    @abstractmethod
    def validate_url(self, url: str) -> bool:
        """Valida una URL contra SSRF"""
        pass
    
    @abstractmethod
    def is_internal_ip(self, hostname: str) -> bool:
        """Verifica si una IP es interna"""
        pass