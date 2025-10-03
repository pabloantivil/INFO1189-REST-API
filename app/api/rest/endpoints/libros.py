from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import List
from app.models.schemas import Libro, LibroCreate
from app.services.database import db

router = APIRouter()

security = HTTPBearer()
def verificar_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    
    if token != "secret123":
        raise HTTPException(
            status_code=401,
            detail="Token no valido"
        )
    
    return {"valid": True, "token": token}

def crear_libro(libro):
    new_id = len(db) + 1
    
    new_libro = {
        "id": new_id,
        "titulo": libro["titulo"],
        "precio": libro["precio"],
        "detalles": libro.get("detalles", [])
    }
    
    db.append(new_libro)
    return new_libro

@router.post("/libros", response_model=Libro, status_code=201)
def crear_nuevo_libro(libro: LibroCreate, token: dict = Depends(verificar_token)):
    nuevo_libro = crear_libro(libro.model_dump())
    return nuevo_libro
    