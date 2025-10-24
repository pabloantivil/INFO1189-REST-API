"""
Módulo de logging para monitoreo de seguridad y auditoría
"""
import logging
import json
from datetime import datetime
from typing import Any, Dict
from fastapi import Request
import sys

# Configurar el logger principal
logger = logging.getLogger("security_logger")
logger.setLevel(logging.INFO)

# Crear un formateador para los logs
formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s'
)

# Handler para archivo
file_handler = logging.FileHandler("security.log")
file_handler.setFormatter(formatter)

# Handler para consola
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)

# Agregar handlers al logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def log_security_event(
    event_type: str,
    request: Request,
    details: Dict[str, Any],
    level: str = "INFO"
) -> None:
    """
    Registra eventos de seguridad con información detallada.
    
    Args:
        event_type (str): Tipo de evento (auth, access, error, etc.)
        request (Request): Objeto Request de FastAPI
        details (Dict[str, Any]): Detalles específicos del evento
        level (str): Nivel de logging (INFO, WARNING, ERROR, CRITICAL)
    """
    log_data = {
        "timestamp": datetime.utcnow().isoformat(),
        "event_type": event_type,
        "client_ip": request.client.host,
        "method": request.method,
        "url": str(request.url),
        "headers": dict(request.headers),
        "details": details
    }
    
    log_method = getattr(logger, level.lower())
    log_method(json.dumps(log_data))