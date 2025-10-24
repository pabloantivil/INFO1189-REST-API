from collections.abc import AsyncIterator
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core import config
from app.api.rest.endpoints import products
from app.api.graphql.queries.product_queries import schema_graphql
from strawberry.fastapi import GraphQLRouter
from fastapi_cache.backends.inmemory import InMemoryBackend
from fastapi_cache import FastAPICache
from contextlib import asynccontextmanager
from app.middleware.security import SecurityMiddleware
from app.core.services.security_services import (
    InMemoryRateLimiter,
    FileSecurityLogger,
    SSRFURLValidator
)

def create_application() -> FastAPI:
    @asynccontextmanager
    async def lifespan(_: FastAPI) -> AsyncIterator[None]:
        FastAPICache.init(InMemoryBackend(), prefix="fastapi-cache")
        yield


    """
    Factory function para crear la aplicación FastAPI.
    """
    app = FastAPI(
        title=config.APP_NAME,
        version=config.API_VERSION,
        description="API REST para evaluación INFO1189 - Implementa principios REST y Clean Architecture",
        docs_url="/docs",
        redoc_url="/redoc",
        lifespan=lifespan
    )

    # CORS (Cross-Origin Resource Sharing) con configuración segura
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000", "http://localhost:8000"],  # Incluir localhost para docs
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS"],
        allow_headers=["*"],
        expose_headers=["*"],
        max_age=600,
    )
    
    # Middleware de seguridad personalizado
    app.add_middleware(
        SecurityMiddleware,
        rate_limiter=InMemoryRateLimiter(requests_per_second=10),
        security_logger=FileSecurityLogger(log_file="security.log"),
        url_validator=SSRFURLValidator(
            allowed_schemes=['https', 'http'],  # Permitir http para desarrollo local
            allowed_hosts=['localhost', '127.0.0.1'] 
        )
    )
    
    # Incluir routers de endpoints
    app.include_router(
        products.router,
        prefix=f"/api/{config.API_VERSION}",
        tags=["products"]
    )

    # Incluir graphql

    graphql_app = GraphQLRouter(schema_graphql)

    app.include_router(
        graphql_app,
        prefix=f"/graphql",
    )
    
    return app

# Crear instancia de la aplicación
app = create_application()

@app.get("/")
async def root():
    """
    Endpoint raíz con información básica.
    Principios REST: recurso identificado, autodescriptivo.
    """
    return {
        "message": "API REST - Evaluación INFO1189",
        "version": config.API_VERSION,
        "docs": "/docs",
        "redoc": "/redoc",
        "endpoints": {
            "products": f"/api/{config.API_VERSION}/products",
            "health": f"/api/{config.API_VERSION}/health"
        }
    }

@app.get(f"/api/{config.API_VERSION}/health")
async def health_check():
    """
    Endpoint de health check.
    Útil para verificar que la API está funcionando.
    """
    return {
        "status": "healthy",
        "timestamp": "2024-10-01T00:00:00Z",
        "version": config.API_VERSION
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=config.DEBUG
    )