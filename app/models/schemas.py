from pydantic import BaseModel
from typing import List


class Informacion(BaseModel):
    campo: str
    valor: str

class Detalles(BaseModel):
    categoria: str
    informacion: List[Informacion]
    
class Libro(BaseModel):
    id: int
    titulo: str
    precio: float
    detalles: List[Detalles]
    
class LibroCreate(BaseModel):
    titulo: str
    precio: float
    detalles: List[Detalles] = []
    