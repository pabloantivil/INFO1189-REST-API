from fastapi import Request, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.config import SECRET_KEY

# https://fastapi.tiangolo.com/reference/security/#fastapi.security.HTTPBearer--usage

security = HTTPBearer()

def verificar_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    
    if token != "secret123":
        raise HTTPException(
            status_code=401,
            detail="Token no valido"
        )
    
    return {"valid": True, "token": token}