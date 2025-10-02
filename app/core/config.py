import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Configuración de la aplicación
APP_NAME = os.getenv("APP_NAME")
DEBUG = os.getenv("DEBUG", "false").lower() == "true"
API_VERSION = os.getenv("API_VERSION")

# Configuración JWT (variables sensibles)
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

# Configuración del servidor
HOST = os.getenv("HOST")
PORT = int(os.getenv("PORT"))

# Validaciones de seguridad - Variables obligatorias
if not APP_NAME:
    raise ValueError("APP_NAME no está definido en las variables de entorno")

if not API_VERSION:
    raise ValueError("API_VERSION no está definido en las variables de entorno")

if not SECRET_KEY:
    raise ValueError("SECRET_KEY no está definido en las variables de entorno")

if not ALGORITHM:
    raise ValueError("ALGORITHM no está definido en las variables de entorno")

if not HOST:
    raise ValueError("HOST no está definido en las variables de entorno")