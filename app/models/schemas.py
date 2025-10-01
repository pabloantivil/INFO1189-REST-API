from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class ProductBase(BaseModel):
    """
    Esquema base del producto
    """
    name: str = Field(..., min_length=1, max_length=100, description="Nombre del producto")
    description: str = Field(..., min_length=1, max_length=500, description="Descripción del producto")
    price: float = Field(..., gt=0, description="Precio del producto")
    category: str = Field(..., min_length=1, max_length=50, description="Categoría del producto")

class ProductCreate(ProductBase):
    """
    Esquema para creación de productos.
    """
    pass

class ProductUpdate(BaseModel):
    """
    Esquema para actualización parcial de productos.
    """
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, min_length=1, max_length=500)
    price: Optional[float] = Field(None, gt=0)
    category: Optional[str] = Field(None, min_length=1, max_length=50)

class ProductResponse(ProductBase):
    """
    Esquema de respuesta con estructura JSON de máximo 3 niveles.
    Nivel 1: Producto
    Nivel 2: Metadatos, categoría info
    Nivel 3: Links de hipermedia
    """
    id: int = Field(..., description="ID único del producto")
    created_at: datetime = Field(..., description="Fecha de creación")
    updated_at: Optional[datetime] = Field(None, description="Fecha de última actualización")
    
    # Nivel 2: Metadatos de categoría
    category_info: dict = Field(default_factory=lambda: {
        "name": "",
        "links": {  # Nivel 3: Enlaces hipermedia
            "category_products": "/api/v1/products?category=",
            "category_details": "/api/v1/categories/"
        }
    })
    
    # Nivel 2: Enlaces hipermedia del producto
    links: dict = Field(default_factory=lambda: {
        "self": "/api/v1/products/",
        "update": "/api/v1/products/",
        "delete": "/api/v1/products/"
    })
    
    class Config:
        from_attributes = True

class ProductList(BaseModel):
    """
    Esquema para lista de productos con metadatos.
    """
    products: List[ProductResponse] = Field(..., description="Lista de productos")
    total: int = Field(..., description="Total de productos")
    page: int = Field(default=1, description="Página actual")
    per_page: int = Field(default=10, description="Productos por página")
    
    # Nivel 2: Enlaces de navegación
    navigation: dict = Field(default_factory=lambda: {
        "links": {  # Nivel 3: Enlaces hipermedia
            "first": "/api/v1/products?page=1",
            "last": "/api/v1/products?page=",
            "next": None,
            "prev": None
        }
    })

# Esquemas para JWT
class Token(BaseModel):
    """Esquema para respuesta de token JWT"""
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    """Esquema para datos del token"""
    username: Optional[str] = None