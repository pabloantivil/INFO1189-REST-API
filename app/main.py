from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.endpoints import products

def create_application() -> FastAPI:
    """
    Factory function para crear la aplicación FastAPI.
    """
    app = FastAPI(
        title=settings.app_name,
        version=settings.api_version,
        description="API REST INFO1189 - Implementa principios REST y Clean Architecture",
        docs_url="/docs",  # Documentación automática en /docs
        redoc_url="/redoc"  # Documentación alternativa en /redoc
    )
    
    # Configurar CORS (Cross-Origin Resource Sharing)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # En producción usar dominios específicos
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Incluir routers de endpoints
    app.include_router(
        products.router,
        prefix=f"/api/{settings.api_version}",
        tags=["products"]
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
        "version": settings.api_version,
        "docs": "/docs",
        "redoc": "/redoc",
        "endpoints": {
            "products": f"/api/{settings.api_version}/products",
            "health": f"/api/{settings.api_version}/health"
        }
    }

@app.get(f"/api/{settings.api_version}/health")
async def health_check():
    """
    Endpoint de health check.
    Útil para verificar que la API está funcionando.
    """
    return {
        "status": "healthy",
        "timestamp": "2024-10-01T00:00:00Z",
        "version": settings.api_version
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug
    )