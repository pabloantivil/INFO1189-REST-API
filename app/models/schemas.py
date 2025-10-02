from pydantic import BaseModel
from typing import List

class Detalle(BaseModel):
    id: int
    atributo: str
    valor: str

class Especificacion(BaseModel):
    id: int
    categoria: str
    detalles: List[Detalle]

class Producto(BaseModel):
    id: int
    nombre: str
    precio: float
    especificaciones: List[Especificacion]

class ProductoCreate(BaseModel):
    nombre: str
    precio: float
    especificaciones: List[Especificacion] = []