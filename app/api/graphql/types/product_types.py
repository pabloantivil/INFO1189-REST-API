from typing import List
import strawberry
from app.models.schemas import Detalle, Especificacion, Producto, ProductoCreate

# Esto es igual que un schema
# https://strawberry.rocks/docs


@strawberry.experimental.pydantic.type(model=Detalle)
class DetalleType:
    id: strawberry.auto
    atributo: strawberry.auto
    valor: strawberry.auto

@strawberry.experimental.pydantic.type(model=Especificacion)
class EspecificacionType:
    id: strawberry.auto
    categoria: strawberry.auto
    detalles: List[DetalleType]

@strawberry.experimental.pydantic.type(model=Producto)
class ProductoType:
    id: strawberry.auto
    nombre: strawberry.auto
    precio: strawberry.auto
    especificaciones: List[EspecificacionType]

@strawberry.experimental.pydantic.input(model=ProductoCreate)
class ProductoCreateType:
    nombre: strawberry.auto
    precio: strawberry.auto
    especificaciones: List[EspecificacionType]
