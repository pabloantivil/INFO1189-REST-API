from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core import config
from app.api.endpoints import products

def create_application() -> FastAPI:
    """
    Factory function para crear la aplicación FastAPI.
    """
    app = FastAPI(
    title=config.APP_NAME,
    version=config.API_VERSION,
    description="API REST para evaluación INFO1189 - Implementa principios REST y Clean Architecture",
    docs_url="/docs",
    redoc_url="/redoc"
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
    prefix=f"/api/{config.API_VERSION}",
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