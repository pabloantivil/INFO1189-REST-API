# Aquí se definirán las funciones para interactuar con la base de datos
# Por simplicidad, usaremos una lista en memoria como "base de datos"

# Base de datos de productos tecnológicos
db = [
    {
        "id": 1,
        "nombre": "MacBook Air M2 13' 256GB",
        "precio": 1299990.00,
        "categoria": "Laptops",
        "marca": "Apple",
        "stock": 15,
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
                    {"atributo": "Teleobjetivo", "valor": "12MP f/2.8 (3x zoom)"}
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
                    {"atributo": "Teleobjetivo", "valor": "50MP f/3.4 (5x zoom óptico)"},
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
    {
        "id": 4,
        "nombre": "PlayStation 5 Slim 1TB",
        "precio": 599990.00,
        "categoria": "Consolas",
        "marca": "Sony",
        "stock": 5,
        "especificaciones": [
            {
                "grupo": "Hardware",
                "detalles": [
                    {"atributo": "CPU", "valor": "AMD Zen 2 de 8 núcleos a 3.5GHz"},
                    {"atributo": "GPU", "valor": "AMD RDNA 2 con 10.28 TFLOPs"},
                    {"atributo": "RAM", "valor": "16GB GDDR6"}
                ]
            },
            {
                "grupo": "Almacenamiento",
                "detalles": [
                    {"atributo": "SSD interno", "valor": "1TB NVMe PCIe 4.0"},
                    {"atributo": "Velocidad", "valor": "5.5GB/s sin comprimir"},
                    {"atributo": "Expandible", "valor": "Slot M.2 adicional"}
                ]
            },
            {
                "grupo": "Multimedia",
                "detalles": [
                    {"atributo": "Resolución", "valor": "Hasta 8K (7680x4320)"},
                    {"atributo": "HDR", "valor": "HDR10, HDR10+, Dolby Vision"},
                    {"atributo": "Audio", "valor": "Dolby Atmos, DTS:X"}
                ]
            }
        ]
    },
    {
        "id": 5,
        "nombre": "Monitor Gaming ASUS ROG Swift 27' 165Hz",
        "precio": 449990.00,
        "categoria": "Monitores",
        "marca": "ASUS",
        "stock": 7,
        "especificaciones": [
            {
                "grupo": "Pantalla",
                "detalles": [
                    {"atributo": "Tamaño", "valor": "27 pulgadas"},
                    {"atributo": "Resolución", "valor": "2560x1440 (QHD)"},
                    {"atributo": "Panel", "valor": "IPS con 1ms GTG"}
                ]
            },
            {
                "grupo": "Gaming",
                "detalles": [
                    {"atributo": "Frecuencia", "valor": "165Hz nativo"},
                    {"atributo": "Adaptive Sync", "valor": "G-SYNC Compatible"},
                    {"atributo": "HDR", "valor": "HDR10 certificado"}
                ]
            },
            {
                "grupo": "Conectividad",
                "detalles": [
                    {"atributo": "DisplayPort", "valor": "1.4 x1"},
                    {"atributo": "HDMI", "valor": "2.0 x2"},
                    {"atributo": "USB Hub", "valor": "3.0 x2"}
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
    
    new_product = {
        "id": new_id,
        "nombre": product_data["nombre"],
        "precio": product_data["precio"],
        "categoria": product_data["categoria"],        
        "marca": product_data["marca"],                  
        "stock": product_data["stock"],                
        "especificaciones": product_data.get("especificaciones", [])
    }
    
    db.append(new_product)
    return new_product

def update_product(product_id: int, product_data: dict) -> dict:
    """Actualizar un producto completamente."""
    for i, p in enumerate(db):
        if p["id"] == product_id:
            updated = {
                "id": product_id,
                "nombre": product_data["nombre"],
                "precio": product_data["precio"],
                "categoria": product_data["categoria"],        
                "marca": product_data["marca"],                  
                "stock": product_data["stock"],                
                "especificaciones": product_data.get("especificaciones", [])
            }
            db[i] = updated
            return updated
    return None

def patch_product(product_id: int, changes: dict) -> dict:
    """Actualizar un producto parcialmente."""
    for i, p in enumerate(db):
        if p["id"] == product_id:
            patched = p.copy()
            if "nombre" in changes:
                patched["nombre"] = changes["nombre"]
            if "precio" in changes:
                patched["precio"] = changes["precio"]
            if "especificaciones" in changes:
                patched["especificaciones"] = changes["especificaciones"]
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