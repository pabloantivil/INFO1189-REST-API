"""
Tests para endpoints de productos de la API REST.
"""

from fastapi.testclient import TestClient
from app.main import app
from app.core.config import API_VERSION, SECRET_KEY

# Crear cliente de pruebas
client = TestClient(app)

# Constantes
BASE_URL = f"/api/{API_VERSION}/products"
TOKEN_VALIDO = SECRET_KEY
HEADERS_AUTH = {"Authorization": f"Bearer {TOKEN_VALIDO}"}


# TEST 1: GET /products - Obtener todos los productos (happy path)
def test_get_all_products_returns_200_and_list():
    """Verifica que GET /products retorna 200 y una lista con productos."""
    response = client.get(BASE_URL)

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1  # Al menos un producto en la DB


# TEST 2: GET /products/{id} con ID existente - Retorna producto (happy path)
def test_get_product_by_id_existing_returns_200():
    """Verifica que GET /products/{id} con ID existente retorna 200 y el producto correcto."""
    # Obtener lista para tomar un ID real
    response = client.get(BASE_URL)
    products = response.json()
    existing_id = products[0]["id"]

    # pedir ese producto específico
    response = client.get(f"{BASE_URL}/{existing_id}")

    assert response.status_code == 200
    product = response.json()
    assert product["id"] == existing_id
    assert "nombre" in product
    assert "precio" in product
    assert "created_at" in product
    assert "updated_at" in product


# TEST 3: GET /products/{id} con ID inexistente - Retorna 404
def test_get_product_by_id_not_found_returns_404():
    """Verifica que GET /products/{id} con ID inexistente retorna 404."""
    id_inexistente = 999999

    response = client.get(f"{BASE_URL}/{id_inexistente}")

    assert response.status_code == 404
    assert "detail" in response.json()


# TEST 4: POST /products sin token - Retorna 401/403 (autenticación requerida)
def test_create_product_without_auth_returns_401():
    """Verifica que POST /products sin Authorization retorna 401 o 403."""
    payload = {
        "nombre": "Producto Test Sin Auth",
        "precio": 99990,
        "categoria": "Test",
        "marca": "TestBrand",
        "stock": 5,
        "especificaciones": []
    }

    response = client.post(BASE_URL, json=payload)

    # FastAPI puede retornar 401 o 403 dependiendo del esquema de seguridad
    assert response.status_code in [401, 403]


# TEST 5: POST /products con token válido - Crea producto y retorna 201
def test_create_product_with_auth_returns_201_and_product():
    """Verifica que POST /products con token válido crea el producto y retorna 201."""
    payload = {
        "nombre": "Producto Test Completo",
        "precio": 149990,
        "categoria": "Accesorios",
        "marca": "TestBrand",
        "stock": 10,
        "especificaciones": []
    }

    response = client.post(BASE_URL, json=payload, headers=HEADERS_AUTH)

    assert response.status_code == 201
    product = response.json()
    assert "id" in product
    assert product["nombre"] == payload["nombre"]
    assert product["precio"] == payload["precio"]
    # Verificar que se generaron timestamps automáticamente
    assert "created_at" in product
    assert "updated_at" in product
    # Verificar que se asignó el actor
    assert "created_by" in product
    assert product["created_by"] == "user:authenticated"
