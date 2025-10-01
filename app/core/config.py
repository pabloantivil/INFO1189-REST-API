from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    """
    Configuración de la aplicación siguiendo principios SOLID.
    SRP: Solo responsabilidad de configuración.
    """
    app_name: str = "REST API - Evaluación INFO1189"
    debug: bool = True
    api_version: str = "v1"
    
    # JWT Configuration
    secret_key: str = "secret123"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # Server Configuration
    host: str = "127.0.0.1"
    port: int = 8000
    
    class Config:
        env_file = ".env"

# Singleton pattern para configuración
settings = Settings()