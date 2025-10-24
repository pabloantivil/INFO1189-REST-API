import re
from fastapi import APIRouter, Depends, HTTPException, Response, Request
from typing import List
from app.models.schemas import Producto, ProductoCreate
from app.services.database import delete_product, get_all_products, get_product_by_id, create_product, patch_product, update_product
from app.utils.token import extraer_actor_desde_token
from app.utils.validators import validate_product_input, sanitize_output
from app.utils.logging import log_security_event
from fastapi_cache.decorator import cache

# Crear el router
router = APIRouter()

# ENDPOINT 1: GET /products - Obtener todos los productos


@router.get("/products", response_model=List[Producto])
#@cache(expire=10)
async def obtener_todos_productos(response: Response, request: Request):
    """
    Obtiene todos los productos con protección contra:
    - A01:2021 - Broken Access Control (via middleware)
    - A05:2021 - Security Misconfiguration (via middleware)
    - A07:2021 - Rate Limiting (via middleware)
    - A09:2021 - Security Logging (logging detallado)
    
    Returns:
        List[Producto]: Lista de productos sanitizada
    """
    try:
        # Log del inicio de la solicitud
        log_security_event(
            "products_list_attempt",
            request,
            {"operation": "list_all"}
        )
        
        productos = get_all_products()
        
        # Log de operación exitosa
        log_security_event(
            "products_listed",
            request,
            {
                "count": len(productos),
                "result": "success"
            }
        )
        
        return sanitize_output(productos)
        
    except Exception as e:
        # Log de error
        log_security_event(
            "products_list_error",
            request,
            {
                "error": str(e),
                "error_type": type(e).__name__
            },
            level="ERROR"
        )
        raise

# ENDPOINT 2: GET /products/{id} - Obtener un producto específico


@router.get("/products/{product_id}", response_model=Producto)
#@cache(expire=10)
async def obtener_producto_por_id(product_id: int, request: Request):
    """
    Obtiene un producto específico con protección contra:
    - A01:2021 - Broken Access Control (via middleware)
    - A05:2021 - Security Misconfiguration (via middleware)
    - A07:2021 - Rate Limiting (via middleware)
    - A09:2021 - Security Logging (logging detallado)
    
    Args:
        product_id (int): ID del producto a obtener
        request (Request): Objeto request de FastAPI
        
    Returns:
        Producto: Producto sanitizado
        
    Raises:
        HTTPException: Si el producto no existe
    """
    try:
        # Log del inicio de la búsqueda
        log_security_event(
            "product_get_attempt",
            request,
            {"product_id": product_id}
        )
        
        producto = get_product_by_id(product_id)

        if not producto:
            # Log de producto no encontrado
            log_security_event(
                "product_not_found",
                request,
                {
                    "product_id": product_id,
                    "result": "not_found"
                },
                level="WARNING"
            )
            raise HTTPException(
                status_code=404,
                detail=f"Producto con ID {product_id} no encontrado"
            )
            
        # Log de búsqueda exitosa
        log_security_event(
            "product_retrieved",
            request,
            {
                "product_id": product_id,
                "result": "success"
            }
        )
        
        return sanitize_output(producto)
        
    except Exception as e:
        if isinstance(e, HTTPException):
            raise
            
        # Log de error
        log_security_event(
            "product_get_error",
            request,
            {
                "product_id": product_id,
                "error": str(e),
                "error_type": type(e).__name__
            },
            level="ERROR"
        )
        raise

# ENDPOINT 3: POST /products - Crear un nuevo producto


@router.post("/products", response_model=Producto, status_code=201)
async def crear_producto(
    producto_data: ProductoCreate,
    request: Request,
    actor: str = Depends(extraer_actor_desde_token)
):
    """
    Crea un nuevo producto con protección contra:
    - A03:2021 - Injection (validación de entrada)
    - A04:2021 - Insecure Design (validación de datos)
    - A05:2021 - Security Misconfiguration (via middleware)
    - A07:2021 - Rate Limiting (via middleware)
    - A09:2021 - Security Logging (logging detallado)
    - A10:2021 - SSRF (validación de URLs)
    
    Args:
        producto_data (ProductoCreate): Datos del producto a crear
        request (Request): Objeto request de FastAPI
        actor (str): Actor que realiza la operación
        
    Returns:
        Producto: Producto creado y sanitizado
        
    Raises:
        HTTPException: Si los datos contienen contenido malicioso
    """
    try:
        # Log del intento de creación
        log_security_event(
            "product_create_attempt",
            request,
            {"actor": actor, "product_data": producto_data.model_dump()}
        )
        
        # Validar entrada contra inyecciones
        validate_product_input(producto_data.model_dump())
        
        
        nuevo_producto = create_product(
            producto_data.model_dump(), created_by=actor)
        
        # Log de creación exitosa
        log_security_event(
            "product_created",
            request,
            {
                "actor": actor,
                "product_id": nuevo_producto.get("id"),
                "result": "success"
            }
        )
        
        return sanitize_output(nuevo_producto)
        
    except Exception as e:
        # Log de error en la creación
        log_security_event(
            "product_create_error",
            request,
            {
                "actor": actor,
                "error": str(e),
                "error_type": type(e).__name__
            },
            level="ERROR"
        )
        raise

# PUT /products/{id} - Actualizar producto completo


@router.put("/products/{product_id}", response_model=Producto)
async def update_product_endpoint(
    product_id: int,
    producto: ProductoCreate,
    request: Request,
    actor: str = Depends(extraer_actor_desde_token)
):
    """
    Actualiza un producto completamente con protección contra:
    - A01:2021 - Broken Access Control (via middleware)
    - A03:2021 - Injection (validación de entrada)
    - A04:2021 - Insecure Design (validación de datos)
    - A05:2021 - Security Misconfiguration (via middleware)
    - A07:2021 - Rate Limiting (via middleware)
    - A09:2021 - Security Logging (logging detallado)
    
    Args:
        product_id (int): ID del producto a actualizar
        producto (ProductoCreate): Nuevos datos del producto
        request (Request): Objeto request de FastAPI
        actor (str): Actor que realiza la operación
        
    Returns:
        Producto: Producto actualizado y sanitizado
        
    Raises:
        HTTPException: Si el producto no existe o los datos contienen contenido malicioso
    """
    try:
        # Log del intento de actualización
        log_security_event(
            "product_update_attempt",
            request,
            {
                "product_id": product_id,
                "actor": actor,
                "update_data": producto.model_dump()
            }
        )
        
        product = get_product_by_id(product_id)
        if not product:
            # Log de producto no encontrado
            log_security_event(
                "product_not_found",
                request,
                {
                    "product_id": product_id,
                    "actor": actor,
                    "result": "not_found"
                },
                level="WARNING"
            )
            raise HTTPException(
                status_code=404,
                detail=f"Producto con ID {product_id} no encontrado"
            )
        
        # Validar entrada contra inyecciones
        validate_product_input(producto.model_dump())
        
        updated_product = update_product(product_id, producto.model_dump(), updated_by=actor)
        
        # Log de actualización exitosa
        log_security_event(
            "product_updated",
            request,
            {
                "product_id": product_id,
                "actor": actor,
                "result": "success"
            }
        )
        
        return sanitize_output(updated_product)
        
    except Exception as e:
        if isinstance(e, HTTPException):
            raise
            
        # Log de error en la actualización
        log_security_event(
            "product_update_error",
            request,
            {
                "product_id": product_id,
                "actor": actor,
                "error": str(e),
                "error_type": type(e).__name__
            },
            level="ERROR"
        )
        raise

# PATCH /products/{id} - Actualizar producto parcialmente


@router.patch("/products/{product_id}", response_model=Producto)
async def patch_product_endpoint(
    product_id: int,
    changes: dict,
    request: Request,
    actor: str = Depends(extraer_actor_desde_token)
):
    """
    Actualiza un producto parcialmente con protección contra:
    - A01:2021 - Broken Access Control (via middleware)
    - A03:2021 - Injection (validación de entrada)
    - A04:2021 - Insecure Design (validación de datos)
    - A05:2021 - Security Misconfiguration (via middleware)
    - A07:2021 - Rate Limiting (via middleware)
    - A09:2021 - Security Logging (logging detallado)
    
    Args:
        product_id (int): ID del producto a actualizar
        changes (dict): Cambios parciales a aplicar
        request (Request): Objeto request de FastAPI
        actor (str): Actor que realiza la operación
        
    Returns:
        Producto: Producto actualizado y sanitizado
        
    Raises:
        HTTPException: Si el producto no existe o los datos contienen contenido malicioso
    """
    try:
        # Log del intento de actualización parcial
        log_security_event(
            "product_patch_attempt",
            request,
            {
                "product_id": product_id,
                "actor": actor,
                "changes": changes
            }
        )
        
        product = get_product_by_id(product_id)
        if not product:
            # Log de producto no encontrado
            log_security_event(
                "product_not_found",
                request,
                {
                    "product_id": product_id,
                    "actor": actor,
                    "result": "not_found"
                },
                level="WARNING"
            )
            raise HTTPException(
                status_code=404,
                detail=f"Producto con ID {product_id} no encontrado"
            )
        
        # Validar entrada contra inyecciones
        validate_product_input(changes)
        
        updated_product = patch_product(product_id, changes, updated_by=actor)
        
        # Log de actualización parcial exitosa
        log_security_event(
            "product_patched",
            request,
            {
                "product_id": product_id,
                "actor": actor,
                "result": "success",
                "fields_updated": list(changes.keys())
            }
        )
        
        return sanitize_output(updated_product)
        
    except Exception as e:
        if isinstance(e, HTTPException):
            raise
            
        # Log de error en la actualización parcial
        log_security_event(
            "product_patch_error",
            request,
            {
                "product_id": product_id,
                "actor": actor,
                "error": str(e),
                "error_type": type(e).__name__
            },
            level="ERROR"
        )
        raise

# DELETE /products/{id} - Eliminar producto


@router.delete("/products/{product_id}", status_code=204)
async def delete_product_endpoint(
    product_id: int,
    request: Request,
    actor: str = Depends(extraer_actor_desde_token)
):
    """
    Elimina un producto con protección contra:
    - A01:2021 - Broken Access Control (via middleware)
    - A05:2021 - Security Misconfiguration (via middleware)
    - A07:2021 - Rate Limiting (via middleware)
    - A09:2021 - Security Logging (logging detallado)
    
    Args:
        product_id (int): ID del producto a eliminar
        request (Request): Objeto request de FastAPI
        actor (str): Actor que realiza la operación
        
    Returns:
        None
        
    Raises:
        HTTPException: Si el producto no existe
    """
    try:
        # Log del intento de eliminación
        log_security_event(
            "product_delete_attempt",
            request,
            {
                "product_id": product_id,
                "actor": actor
            }
        )
        
        product = get_product_by_id(product_id)
        if not product:
            # Log de producto no encontrado
            log_security_event(
                "product_not_found",
                request,
                {
                    "product_id": product_id,
                    "actor": actor,
                    "result": "not_found"
                },
                level="WARNING"
            )
            raise HTTPException(
                status_code=404,
                detail=f"Producto con ID {product_id} no encontrado"
            )
            
        # Guardar datos del producto antes de eliminar para el log
        product_data = {
            "id": product_id,
            "name": product.get("name", "unknown"),
            "last_modified": product.get("updated_at", "unknown")
        }
        
        delete_product(product_id)
        
        # Log de eliminación exitosalog_security_event
        log_security_event(
            "product_deleted",
            request,
            {
                "product_id": product_id,
                "actor": actor,
                "product_info": product_data,
                "result": "success"
            }
        )
        
        return None
        
    except Exception as e:
        if isinstance(e, HTTPException):
            raise
            
        # Log de error en la eliminación
        log_security_event(
            "product_delete_error",
            request,
            {
                "product_id": product_id,
                "actor": actor,
                "error": str(e),
                "error_type": type(e).__name__
            },
            level="ERROR"
        )
        raise
