
import strawberry
from typing import List
from app.services.database import get_all_products
from app.api.graphql.types.product_types import ProductoType
from app.models.schemas import Producto
from app.api.graphql.mutations.product_mutations import Mutation


# Resolvers
def resolve_all_products() -> List[Producto]:
    items = get_all_products()
    return [Producto(**p) for p in items]


@strawberry.type
class Query:
    products: List[ProductoType] = strawberry.field(resolver=resolve_all_products)


schema_graphql = strawberry.Schema(query=Query, mutation=Mutation)