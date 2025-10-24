from fastapi import APIRouter, Depends, HTTPException, Response
from typing import List, Optional
from app.models.schemas import Producto, ProductoCreate
from app.services.database import delete_product, get_all_products, get_product_by_id, create_product, patch_product, update_product
from app.utils.token import verificar_token, extraer_actor_desde_token
from fastapi_cache.decorator import cache

# Crear el router
router = APIRouter()

# ENDPOINT 1: GET /products - Obtener todos los productos


@router.get("/products", response_model=List[Producto])
# @cache(expire=10)  # Desactivado para tests
async def obtener_todos_productos(response: Response):
    productos = get_all_products()
    return productos

# ENDPOINT 2: GET /products/{id} - Obtener un producto específico


@router.get("/products/{product_id}", response_model=Producto)
# @cache(expire=10)  # Desactivado para tests
async def obtener_producto_por_id(product_id: int):
    producto = get_product_by_id(product_id)

    if not producto:
        raise HTTPException(
            status_code=404,
            detail=f"Producto con ID {product_id} no encontrado"
        )
    return producto

# ENDPOINT 3: POST /products - Crear un nuevo producto


@router.post("/products", response_model=Producto, status_code=201)
async def crear_producto(
    producto_data: ProductoCreate,
    actor: str = Depends(extraer_actor_desde_token)
):
    nuevo_producto = create_product(
        producto_data.model_dump(), created_by=actor)
    return nuevo_producto

# PUT /products/{id} - Actualizar producto completo


@router.put("/products/{product_id}", response_model=Producto)
async def update_product_endpoint(
    product_id: int,
    producto: ProductoCreate,
    actor: str = Depends(extraer_actor_desde_token)
):
    """Actualiza un producto completamente."""

    product = get_product_by_id(product_id)
    if not product:
        raise HTTPException(
            status_code=404,
            detail=f"Producto con ID {product_id} no encontrado"
        )

    return update_product(product_id, producto.model_dump(), updated_by=actor)

# PATCH /products/{id} - Actualizar producto parcialmente


@router.patch("/products/{product_id}", response_model=Producto)
async def patch_product_endpoint(
    product_id: int,
    changes: dict,
    actor: str = Depends(extraer_actor_desde_token)
):
    """Actualiza un producto parcialmente."""
    product = get_product_by_id(product_id)
    if not product:
        raise HTTPException(
            status_code=404,
            detail=f"Producto con ID {product_id} no encontrado"
        )
    return patch_product(product_id, changes, updated_by=actor)

# DELETE /products/{id} - Eliminar producto


@router.delete("/products/{product_id}", status_code=204)
async def delete_product_endpoint(product_id: int):
    """Elimina un producto."""
    product = get_product_by_id(product_id)
    if not product:
        raise HTTPException(
            status_code=404,
            detail=f"Producto con ID {product_id} no encontrado"
        )
    delete_product(product_id)
    return None
