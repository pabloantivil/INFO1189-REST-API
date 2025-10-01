# INFO1189-REST-API 🚀

API REST desarrollada con **FastAPI** para el curso INFO1189. Este proyecto implementa los principios fundamentales de la arquitectura REST, incluyendo Clean Architecture, manejo de schemas con Pydantic, y documentación automática.

## 📖 Descripción del Proyecto

Esta API REST está diseñada siguiendo los **principios REST** y las mejores prácticas de desarrollo:

- ✅ **Arquitectura RESTful**: Implementa los 6 principios de REST
- ✅ **Clean Architecture**: Separación clara de responsabilidades
- ✅ **Documentación automática**: Con FastAPI y OpenAPI
- ✅ **Validación de datos**: Usando Pydantic schemas
- ✅ **Configuración centralizada**: Variables de entorno y settings
- ✅ **CORS habilitado**: Para desarrollo frontend
- ✅ **Estructura JSON de máximo 3 niveles**: Siguiendo estándares REST
- ✅ **Health Check**: Endpoint para monitoreo

## 🏗️ Arquitectura del Proyecto

```
INFO1189-REST-API/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Punto de entrada de la aplicación
│   ├── api/                    # Capa de API
│   │   └── endpoints/
│   │       ├── __init__.py
│   │       └── products.py     # Endpoints de productos
│   ├── core/                   # Configuración central
│   │   ├── __init__.py
│   │   └── config.py          # Settings y configuración
│   ├── models/                 # Modelos y schemas
│   │   ├── __init__.py
│   │   └── schemas.py         # Schemas de Pydantic
│   └── services/              # Lógica de negocio
│       ├── __init__.py
│       └── database.py        # Servicios de base de datos
├── requirements.txt           # Dependencias del proyecto
├── README.md                 # Este archivo
└── README-Instrucciones.md   # Guía teórica de REST
```

## 🛠️ Tecnologías Utilizadas

- **FastAPI**: Framework web moderno y rápido para Python
- **Uvicorn**: Servidor ASGI para desarrollo
- **Pydantic**: Validación de datos y settings management
- **Python-JOSE**: Manejo de tokens JWT
- **Passlib**: Hashing de contraseñas
- **Strawberry-GraphQL**: Soporte para GraphQL (futuro)

## 🚀 Instalación y Configuración

### Prerequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### 1. Clonar el Repositorio

```powershell
git clone https://github.com/pabloantivil/INFO1189-REST-API.git
cd INFO1189-REST-API
```

### 2. Crear y Activar Entorno Virtual

**Crear el entorno virtual:**

```powershell
python -m venv venv
```

**Activar el entorno virtual:**

```powershell
# En Windows PowerShell
.\venv\Scripts\Activate.ps1

# En Windows CMD
venv\Scripts\activate.bat
```

**Para desactivar el entorno virtual:**

```powershell
deactivate
```

### 3. Instalar Dependencias

```powershell
pip install -r requirements.txt
```

### 4. Configurar Variables de Entorno (Opcional)

Crear un archivo `.env` en la raíz del proyecto:

```env
APP_NAME="REST API - Evaluación INFO1189"
DEBUG=true
API_VERSION="v1"
SECRET_KEY="secret123"
HOST="127.0.0.1"
PORT=8000
```

## ▶️ Cómo Ejecutar la Aplicación

### Opción 1: Usando Python directamente

```powershell
python -m app.main
```

### Opción 2: Usando Uvicorn

```powershell
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Opción 3: Usando el script de desarrollo

```powershell
python app/main.py
```

## 🧪 Testing

Para probar la API, puedes usar:

1. **Swagger UI**: Navega a `http://localhost:8000/docs`
2. **curl**:
   ```powershell
   curl http://localhost:8000/api/v1/health
   ```
3. **Postman** o **Insomnia**

## 📚 Recursos Adicionales

- [Documentación de FastAPI](https://fastapi.tiangolo.com/)
- [Guía de REST API](./README-Instrucciones.md)
- [Principios REST](https://restfulapi.net/)

---

_Desarrollado para INFO1189 - Universidad Católica de Temuco_
