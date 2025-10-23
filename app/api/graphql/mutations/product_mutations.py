import strawberry
from app.api.graphql.types.product_types import ProductoType, ProductoCreateType
from app.models.schemas import Producto
from app.services.database import create_product


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_product(self, producto: ProductoCreateType) -> ProductoType:
        """Crear un nuevo producto via GraphQL."""
        # Nota: GraphQL no tiene autenticación en esta demo
        # En producción: extraer actor desde context (info.context.user)
        new_product = create_product(
            producto.to_pydantic().model_dump(),
            created_by="graphql:anonymous"
        )
        return Producto(**new_product)
