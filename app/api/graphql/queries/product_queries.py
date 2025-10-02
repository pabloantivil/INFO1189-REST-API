
import strawberry
from typing import List, Optional
from app.services.database import get_all_products, get_product_by_id
from app.api.graphql.types.product_types import ProductoType
from app.models.schemas import Producto


# Resolvers
def resolve_all_products() -> List[Producto]:
    items = get_all_products()
    return [Producto(**p) for p in items]


def resolve_product(product_id: int) -> Optional[Producto]:
    p = get_product_by_id(product_id)
    return Producto(**p) if p else None


@strawberry.type
class Query:
    products: List[ProductoType] = strawberry.field(resolver=resolve_all_products)
    product: Optional[ProductoType] = strawberry.field(resolver=resolve_product)


schema_graphql = strawberry.Schema(query=Query)