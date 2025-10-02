import strawberry
from app.api.graphql.types.product_types import ProductoType, ProductoCreateType
from app.services.database import create_product
from app.services.database import db

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_product(self, producto: ProductoCreateType) -> ProductoType:
        # Convertir ProductoCreateType a dict compatible con create_product
        specs = []
        for s in getattr(producto, "especificaciones", []):
            detalles = []
            for d in getattr(s, "detalles", []):
                detalles.append({"id": getattr(d, "id", None), "atributo": getattr(d, "atributo", None), "valor": getattr(d, "valor", None)})
            specs.append({"id": getattr(s, "id", None), "categoria": getattr(s, "categoria", None), "detalles": detalles})

        payload = {
            "nombre": getattr(producto, "nombre", None),
            "precio": getattr(producto, "precio", None),
            "especificaciones": specs,
        }

        new = create_product(payload)
        return ProductoType(id=new.get("id"), nombre=new.get("nombre"), precio=new.get("precio"), especificaciones=new.get("especificaciones", []))