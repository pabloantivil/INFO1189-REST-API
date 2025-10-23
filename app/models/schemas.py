from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class Detalles(BaseModel):
    atributo: str
    valor: str

class Especificaciones(BaseModel):
    grupo: str
    detalles: List[Detalles]

class Producto(BaseModel):
    id: int
    nombre: str
    precio: float
    categoria: str
    marca: str
    stock: int
    especificaciones: List[Especificaciones]
    created_at: str 
    updated_at: str  
    created_by: Optional[str] = None # Identificador del creador
    updated_by: Optional[str] = None # Identificador del último modificador


class ProductoCreate(BaseModel):
    nombre: str
    precio: float
    categoria: str
    marca: str
    stock: int
    especificaciones: List[Especificaciones] = []
