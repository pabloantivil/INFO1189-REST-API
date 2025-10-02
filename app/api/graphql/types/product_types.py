from typing import List
import strawberry
from app.models.schemas import Detalle, Especificacion, Producto, ProductoCreate

# Tipos de salida (queries)
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


# Tipos de entrada (mutations) - deben ser Input types en GraphQL
@strawberry.experimental.pydantic.input(model=Detalle)
class DetalleInputType:
    id: strawberry.auto
    atributo: strawberry.auto
    valor: strawberry.auto


@strawberry.experimental.pydantic.input(model=Especificacion)
class EspecificacionInputType:
    id: strawberry.auto
    categoria: strawberry.auto
    detalles: List[DetalleInputType]


@strawberry.experimental.pydantic.input(model=ProductoCreate)
class ProductoCreateType:
    nombre: strawberry.auto
    precio: strawberry.auto
    especificaciones: List[EspecificacionInputType]
