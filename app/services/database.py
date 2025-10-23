# Aquí se definirán las funciones para interactuar con la base de datos
# Por simplicidad, usaremos una lista en memoria como "base de datos"

from datetime import datetime, timezone


def _get_utc_timestamp() -> str:
    """Helper para generar timestamp UTC en formato ISO8601"""
    return datetime.now(timezone.utc).isoformat()


# Base de datos de productos tecnológicos
db = [
    {
        "id": 1,
        "nombre": "MacBook Air M2 13' 256GB",
        "precio": 1299990.00,
        "categoria": "Laptops",
        "marca": "Apple",
        "stock": 15,
        "created_at": "2025-09-15T10:30:00+00:00",
        "updated_at": "2025-10-20T14:20:00+00:00",
        "created_by": "admin@techstore.cl",
        "updated_by": "admin@techstore.cl",
        "especificaciones": [
            {
                "grupo": "Procesador",
                "detalles": [
                    {"atributo": "Chip", "valor": "Apple M2 de 8 núcleos"},
                    {"atributo": "GPU", "valor": "8 núcleos integrados"},
                    {"atributo": "Neural Engine", "valor": "16 núcleos"}
                ]
            },
            {
                "grupo": "Memoria y Almacenamiento",
                "detalles": [
                    {"atributo": "RAM", "valor": "8GB Unified Memory"},
                    {"atributo": "SSD", "valor": "256GB"},
                    {"atributo": "Expandible", "valor": "No"}
                ]
            },
            {
                "grupo": "Pantalla",
                "detalles": [
                    {"atributo": "Tamaño", "valor": "13.6 pulgadas"},
                    {"atributo": "Resolución", "valor": "2560x1664 Liquid Retina"},
                    {"atributo": "Brillo", "valor": "500 nits"}
                ]
            }
        ]
    },
    {
        "id": 2,
        "nombre": "iPhone 15 Pro 128GB Titanio Natural",
        "precio": 1199990.00,
        "categoria": "Smartphones",
        "marca": "Apple",
        "stock": 8,
        "created_at": "2025-09-18T09:15:00+00:00",
        "updated_at": "2025-10-18T11:45:00+00:00",
        "created_by": "admin@techstore.cl",
        "updated_by": "admin@techstore.cl",
        "especificaciones": [
            {
                "grupo": "Pantalla",
                "detalles": [
                    {"atributo": "Tamaño", "valor": "6.1 pulgadas"},
                    {"atributo": "Tecnología", "valor": "Super Retina XDR OLED"},
                    {"atributo": "Resolución", "valor": "2556x1179 píxeles"}
                ]
            },
            {
                "grupo": "Cámara",
                "detalles": [
                    {"atributo": "Principal", "valor": "48MP f/1.78"},
                    {"atributo": "Ultra angular", "valor": "13MP f/2.2"},
                    {"atributo": "Teleobjetivo",
                        "valor": "12MP f/2.8 (3x zoom)"}
                ]
            },
            {
                "grupo": "Conectividad",
                "detalles": [
                    {"atributo": "Puerto", "valor": "USB-C con Thunderbolt"},
                    {"atributo": "5G", "valor": "Sub-6 GHz"},
                    {"atributo": "WiFi", "valor": "WiFi 6E (802.11ax)"}
                ]
            }
        ]
    },
    {
        "id": 3,
        "nombre": "Samsung Galaxy S24 Ultra 256GB Gris Titanio",
        "precio": 1349990.00,
        "categoria": "Smartphones",
        "marca": "Samsung",
        "stock": 12,
        "created_at": "2025-09-20T13:22:00+00:00",
        "updated_at": "2025-10-21T16:30:00+00:00",
        "created_by": "admin@techstore.cl",
        "updated_by": "inventory@techstore.cl",
        "especificaciones": [
            {
                "grupo": "Pantalla",
                "detalles": [
                    {"atributo": "Tamaño", "valor": "6.8 pulgadas"},
                    {"atributo": "Tecnología", "valor": "Dynamic AMOLED 2X"},
                    {"atributo": "Frecuencia", "valor": "120Hz adaptativos"}
                ]
            },
            {
                "grupo": "Cámara",
                "detalles": [
                    {"atributo": "Principal", "valor": "200MP f/1.7 OIS"},
                    {"atributo": "Teleobjetivo",
                        "valor": "50MP f/3.4 (5x zoom óptico)"},
                    {"atributo": "Ultra angular", "valor": "12MP f/2.2"}
                ]
            },
            {
                "grupo": "Rendimiento",
                "detalles": [
                    {"atributo": "Procesador", "valor": "Snapdragon 8 Gen 3"},
                    {"atributo": "RAM", "valor": "12GB"},
                    {"atributo": "S Pen", "valor": "Incluido"}
                ]
            }
        ]
    },
]


# Funciones para manejar la base de datos
def get_all_products():
    """Obtener todos los productos"""
    return db


def get_product_by_id(product_id: int):
    """Obtener un producto por ID"""
    for product in db:
        if product["id"] == product_id:
            return product
    return None


def create_product(product_data, created_by: str = None):
    """Crear un nuevo producto"""
    # Generar nuevo ID
    new_id = max([p["id"] for p in db]) + 1 if db else 1

    timestamp = _get_utc_timestamp()

    new_product = {
        "id": new_id,
        "nombre": product_data["nombre"],
        "precio": product_data["precio"],
        "categoria": product_data["categoria"],
        "marca": product_data["marca"],
        "stock": product_data["stock"],
        "especificaciones": product_data.get("especificaciones", []),
        "created_at": timestamp,
        "updated_at": timestamp,
        "created_by": created_by,
        "updated_by": created_by
    }

    db.append(new_product)
    return new_product


def update_product(product_id: int, product_data: dict, updated_by: str = None) -> dict:
    """Actualizar un producto completamente."""
    for i, p in enumerate(db):
        if p["id"] == product_id:
            # Preservar campos de auditoría originales
            created_at_original = p["created_at"]
            created_by_original = p["created_by"]

            updated = {
                "id": product_id,
                "nombre": product_data["nombre"],
                "precio": product_data["precio"],
                "categoria": product_data["categoria"],
                "marca": product_data["marca"],
                "stock": product_data["stock"],
                "especificaciones": product_data.get("especificaciones", []),
                "created_at": created_at_original,  # NO cambia
                "updated_at": _get_utc_timestamp(),  # Actualizar timestamp
                "created_by": created_by_original,  # NO cambia
                "updated_by": updated_by  # Actualizar actor
            }
            db[i] = updated
            return updated
    return None


def patch_product(product_id: int, changes: dict, updated_by: str = None) -> dict:
    """Actualizar un producto parcialmente."""
    for i, p in enumerate(db):
        if p["id"] == product_id:
            patched = p.copy()

            # Aplicar cambios permitidos
            if "nombre" in changes:
                patched["nombre"] = changes["nombre"]
            if "precio" in changes:
                patched["precio"] = changes["precio"]
            if "categoria" in changes:
                patched["categoria"] = changes["categoria"]
            if "marca" in changes:
                patched["marca"] = changes["marca"]
            if "stock" in changes:
                patched["stock"] = changes["stock"]
            if "especificaciones" in changes:
                patched["especificaciones"] = changes["especificaciones"]

            # Actualizar metadatos de auditoría
            patched["updated_at"] = _get_utc_timestamp()
            patched["updated_by"] = updated_by
            # created_at y created_by NO cambian

            db[i] = patched
            return patched
    return None


def delete_product(product_id: int) -> bool:
    """Eliminar un producto."""
    for i, p in enumerate(db):
        if p["id"] == product_id:
            db.pop(i)
            return True
    return False
