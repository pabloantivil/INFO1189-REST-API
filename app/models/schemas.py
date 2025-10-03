from pydantic import BaseModel
from typing import List

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

class ProductoCreate(BaseModel):
    nombre: str
    precio: float
    categoria: str
    marca: str
    stock: int
    especificaciones: List[Especificaciones] = []