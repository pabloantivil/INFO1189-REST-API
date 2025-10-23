from fastapi import Request, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.config import SECRET_KEY

# https://fastapi.tiangolo.com/reference/security/#fastapi.security.HTTPBearer--usage

# Esquema de seguridad que espera un token en el encabezado Authorization
security = HTTPBearer()


def verificar_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    if token != SECRET_KEY:
        raise HTTPException(
            status_code=401,
            detail="Token no valido"
        )

    return {"valid": True, "token": token}


def extraer_actor_desde_token(credentials: HTTPAuthorizationCredentials = Depends(security)) -> str:
    """
    Extrae el identificador del actor desde el token JWT.
    Para la demo simplificada, retorna un identificador genérico.
    En producción: decodificar JWT y extraer 'sub' o 'email' claim.
    """
    token = credentials.credentials

    if token != SECRET_KEY:
        raise HTTPException(
            status_code=401,
            detail="Token no valido"
        )
        
    # En producción: decodificar el token JWT y extraer el actor
    return "user:authenticated"
