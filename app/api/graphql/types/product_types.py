from typing import List
import strawberry
from app.models.schemas import Detalles, Especificaciones, Producto, ProductoCreate

# Tipos de salida (queries)
@strawberry.experimental.pydantic.type(model=Detalles)
class DetalleType:
    atributo: strawberry.auto
    valor: strawberry.auto


@strawberry.experimental.pydantic.type(model=Especificaciones)
class EspecificacionType:
    grupo: strawberry.auto
    detalles: List[DetalleType]


@strawberry.experimental.pydantic.type(model=Producto)
class ProductoType:
    id: strawberry.auto
    nombre: strawberry.auto
    precio: strawberry.auto
    categoria: strawberry.auto
    marca: strawberry.auto
    stock: strawberry.auto
    especificaciones: List[EspecificacionType]


# Tipos de entrada (mutations) - deben ser Input types en GraphQL
@strawberry.experimental.pydantic.input(model=Detalles)
class DetalleInputType:
    atributo: strawberry.auto
    valor: strawberry.auto


@strawberry.experimental.pydantic.input(model=Especificaciones)
class EspecificacionInputType:
    grupo: strawberry.auto
    detalles: List[DetalleInputType]


@strawberry.experimental.pydantic.input(model=ProductoCreate)
class ProductoCreateType:
    nombre: strawberry.auto
    precio: strawberry.auto
    categoria: strawberry.auto
    marca: strawberry.auto
    stock: strawberry.auto
    especificaciones: List[EspecificacionInputType]
