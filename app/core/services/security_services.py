"""
Implementaciones concretas de servicios de seguridad
"""
import time
import logging
import json
from typing import Dict, Any, List
from fastapi import HTTPException
from app.core.interfaces.security import RateLimiter, SecurityLogger, URLValidator
import ipaddress
from urllib.parse import urlparse
import re

class InMemoryRateLimiter(RateLimiter):
    """Implementación de rate limiting en memoria"""
    
    def __init__(self, requests_per_second: int = 10):
        self.requests: Dict[str, List[float]] = {}
        self.rate_limit = requests_per_second
    
    def check_rate_limit(self, client_ip: str) -> bool:
        current_time = time.time()
        if client_ip in self.requests:
            # Limpiar solicitudes antiguas
            self.requests[client_ip] = [
                ts for ts in self.requests[client_ip]
                if current_time - ts < 1
            ]
            # Verificar límite
            return len(self.requests[client_ip]) < self.rate_limit
        return True
    
    def register_request(self, client_ip: str) -> None:
        current_time = time.time()
        if client_ip not in self.requests:
            self.requests[client_ip] = []
        self.requests[client_ip].append(current_time)

class FileSecurityLogger(SecurityLogger):
    """Implementación de logging en archivo"""
    
    def __init__(self, log_file: str = "security.log"):
        self.logger = logging.getLogger("security_logger")
        
        # Evitar handlers duplicados
        if not self.logger.handlers:
            self.logger.setLevel(logging.INFO)
            
            formatter = logging.Formatter(
                '%(asctime)s - %(levelname)s - %(message)s'
            )
            
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
            
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)
            
        # Evitar propagación de logs
        self.logger.propagate = False
    
    def log_event(self, event_type: str, data: Dict[str, Any], level: str = "INFO") -> None:
        log_data = {
            "timestamp": time.time(),
            "event_type": event_type,
            **data
        }
        log_method = getattr(self.logger, level.lower())
        log_method(json.dumps(log_data))
    
    def log_violation(self, violation_type: str, data: Dict[str, Any]) -> None:
        self.log_event(
            "security_violation",
            {"violation_type": violation_type, **data},
            "WARNING"
        )

class SSRFURLValidator(URLValidator):
    """Implementación de validación de URLs contra SSRF"""
    
    def __init__(self, allowed_schemes: List[str] = None, allowed_hosts: List[str] = None):
        self.allowed_schemes = allowed_schemes or ['https']
        self.allowed_hosts = allowed_hosts or []
    
    def is_internal_ip(self, hostname: str) -> bool:
        try:
            ip = ipaddress.ip_address(hostname)
            return (
                ip.is_private or
                ip.is_loopback or
                ip.is_link_local or
                ip.is_multicast or
                ip.is_reserved
            )
        except ValueError:
            return False
    
    def validate_url(self, url: str) -> bool:
        try:
            parsed = urlparse(url)
            
            if parsed.scheme not in self.allowed_schemes:
                raise HTTPException(
                    status_code=400,
                    detail=f"Esquema no permitido: {parsed.scheme}"
                )
            
            if self.allowed_hosts and parsed.hostname not in self.allowed_hosts:
                raise HTTPException(
                    status_code=400,
                    detail=f"Host no permitido: {parsed.hostname}"
                )
            
            if self.is_internal_ip(parsed.hostname):
                raise HTTPException(
                    status_code=400,
                    detail="No se permiten IPs o hosts internos"
                )
            
            dangerous_patterns = [
                r'127\.0\.0\.1',
                r'localhost',
                r'0\.0\.0\.0',
                r'\[@\]',
                r'0x7f000001',
            ]
            
            url_lower = url.lower()
            for pattern in dangerous_patterns:
                if re.search(pattern, url_lower):
                    raise HTTPException(
                        status_code=400,
                        detail="URL potencialmente peligrosa detectada"
                    )
            
            return True
            
        except Exception as e:
            if isinstance(e, HTTPException):
                raise e
            raise HTTPException(
                status_code=400,
                detail=f"URL inválida: {str(e)}"
            )