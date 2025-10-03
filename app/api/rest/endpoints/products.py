from fastapi import APIRouter, Depends, HTTPException, Response
from typing import List
from app.models.schemas import Producto, ProductoCreate
from app.services.database import get_all_products, get_product_by_id, create_product
from app.utils.token import JWTBearer
from fastapi_cache.decorator import cache

# Crear el router
router = APIRouter()

# ENDPOINT 1: GET /products - Obtener todos los productos
@router.get("/products", response_model=List[Producto])
@cache(expire=60) # 60 seg de caché
async def obtener_todos_productos(response: Response):
    #response.headers["Cache-Control"] = "max-age=3600"  # cacheable por 1 hora
    productos = get_all_products()
    return productos

# ENDPOINT 2: GET /products/{id} - Obtener un producto específico
@router.get("/products/{product_id}", response_model=Producto)
@cache(expire=60) # 60 seg de caché
async def obtener_producto_por_id(product_id: int):
    producto = get_product_by_id(product_id)
    
    if not producto:
        raise HTTPException(
            status_code=404, 
            detail=f"Producto con ID {product_id} no encontrado"
        )
    return producto

# ENDPOINT 3: POST /products - Crear un nuevo producto
# Con inyeccion de dependencias https://testdriven.io/blog/fastapi-jwt-auth/

@router.post("/products", dependencies=[Depends(JWTBearer())], response_model=Producto, status_code=201)
async def crear_producto(producto_data: ProductoCreate):
    nuevo_producto = create_product(producto_data.model_dump())
    return nuevo_producto