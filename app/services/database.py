# Aquí se definirán las funciones para interactuar con la base de datos
# Por simplicidad, usaremos una lista en memoria como "base de datos"

db = [
    {
        "id": 1,
        "nombre": "Laptop Gaming MSI",
        "precio": 1299999.99,
        "especificaciones": [
            {
                "id": 1,
                "categoria": "Procesador",
                "detalles": [
                    {"id": 1, "atributo": "Marca", "valor": "Intel"},
                    {"id": 2, "atributo": "Modelo", "valor": "Core i7-12700H"}
                ]
            },
            {
                "id": 2,
                "categoria": "Memoria",
                "detalles": [
                    {"id": 1, "atributo": "Tipo", "valor": "DDR4"},
                    {"id": 2, "atributo": "Capacidad", "valor": "16GB"}
                ]
            }
        ]
    },
    {
        "id": 2,
        "nombre": "Smartphone Samsung Galaxy",
        "precio": 599999.99,
        "especificaciones": [
            {
                "id": 1,
                "categoria": "Pantalla",
                "detalles": [
                    {"id": 1, "atributo": "Tamaño", "valor": "6.5 pulgadas"},
                    {"id": 2, "atributo": "Resolución", "valor": "1080p"}
                ]
            },
            {
                "id": 2,
                "categoria": "Cámara",
                "detalles": [
                    {"id": 1, "atributo": "Principal", "valor": "108MP"},
                    {"id": 2, "atributo": "Frontal", "valor": "32MP"}
                ]
            }
        ]
    },
    {
        "id": 3,
        "nombre": "Libro Clean Code",
        "precio": 45990.00,
        "especificaciones": [
            {
                "id": 1,
                "categoria": "Autor",
                "detalles": [
                    {"id": 1, "atributo": "Nombre", "valor": "Robert C. Martin"},
                    {"id": 2, "atributo": "Nacionalidad", "valor": "Estadounidense"}
                ]
            },
            {
                "id": 2,
                "categoria": "Editorial",
                "detalles": [
                    {"id": 1, "atributo": "Casa", "valor": "Prentice Hall"},
                    {"id": 2, "atributo": "Año", "valor": "2008"}
                ]
            }
        ]
    }
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

def create_product(product_data):
    """Crear un nuevo producto"""
    # Generar nuevo ID
    new_id = max([p["id"] for p in db]) + 1 if db else 1 
    
    # Crear nuevo producto
    new_product = {
        "id": new_id,
        "nombre": product_data["nombre"],
        "precio": product_data["precio"],
        "especificaciones": product_data.get("especificaciones", [])
    }
    
    db.append(new_product)
    return new_product