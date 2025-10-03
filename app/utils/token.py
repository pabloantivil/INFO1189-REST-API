from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.config import SECRET_KEY

# https://fastapi.tiangolo.com/reference/security/#fastapi.security.HTTPBearer--usage

security = HTTPBearer()

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if credentials.credentials != SECRET_KEY:
                raise HTTPException(status_code=403, detail="Invalid token")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")