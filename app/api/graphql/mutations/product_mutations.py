import strawberry
from app.api.graphql.types.product_types import ProductoType, ProductoCreateType
from app.models.schemas import Producto
from app.services.database import create_product

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_product(self, producto: ProductoCreateType) -> ProductoType:
        """Crear un nuevo producto via GraphQL."""
        # Aprovechar la conversión automática de Pydantic
        new_product = create_product(producto.to_pydantic().model_dump())
        return Producto(**new_product)