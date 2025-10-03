# INFO1189-REST-API 🚀

**API REST completa desarrollada con **FastAPI** para el curso INFO1189.

Esta API implementa un sistema de gestión de productos tecnológicos siguiendo los principios fundamentales de la arquitectura REST, incluyendo Clean Architecture, autenticación JWT, GraphQL, y documentación automática.

## 📖 Descripción del Proyecto

### 🎯 **Funcionalidades Principales**

- ✅ **API REST Completa**: 6 endpoints CRUD (GET, POST, GET by ID, PUT, PATCH, DELETE)
- ✅ **Autenticación JWT**: Protección de endpoints con Bearer Token
- ✅ **GraphQL**: Queries y Mutations implementadas
- ✅ **Base de datos**: Productos tecnologicos
- ✅ **Documentación automática**: Swagger UI y ReDoc
- ✅ **Validaciones**: Schemas Pydantic con tipos estrictos

### 🏗️ **Arquitectura y Principios**

- ✅ **Clean Architecture**: Separación clara de responsabilidades en capas
- ✅ **Principios SOLID**: Código mantenible y extensible
- ✅ **RESTful**: Implementa los 6 principios de REST
- ✅ **JSON 3 niveles**: Estructura de datos optimizada
- ✅ **Variables de entorno**: Configuración segura y flexible
- ✅ **CORS habilitado**: Preparado para integración frontend

## 🏗️ Arquitectura del Proyecto

```
INFO1189-REST-API/
├── app/                        # Aplicación principal
│   ├── main.py                 # Punto de entrada FastAPI
│   ├── api/                    # 🌐 Capa de presentación (API)
│   │   └── endpoints/
│   │       └── products.py     # REST endpoints CRUD completos
│   ├── core/                   # ⚙️ Configuración y utilidades
│   │   └── config.py           # Variables de entorno y settings
│   ├── graphql/                # 🔀 GraphQL Schema y Resolvers
│   │   ├── queries.py          # GraphQL Queries
│   │   ├── mutations.py        # GraphQL Mutations
│   │   └── types.py            # GraphQL Types
│   ├── models/                 # 📋 Modelos y esquemas de datos
│   │   └── schemas.py          # Pydantic schemas (validación)
│   ├── services/               # 💾 Lógica de negocio y datos
│   │   └── database.py         # Base de datos en memoria
│   └── utils/                  # 🔧 Utilidades y herramientas
│       └── token.py            # Manejo de tokens JWT
├── .env.example                # Plantilla de variables de entorno
├── .gitignore                  # Archivos ignorados por Git
├── requirements.txt            # Dependencias Python
├── README.md                   # Este archivo
└── README-Instrucciones.md                 # Guía teórica REST (material de estudio)
```
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

### 4. Configurar Variables de Entorno

**⚠️ IMPORTANTE**: Las variables de entorno son obligatorias para el funcionamiento de la aplicación.

**Crear archivo `.env`** desde la plantilla:

```powershell
# Copiar plantilla
cp .env.example .env
```

## ▶️ Cómo Ejecutar la Aplicación

### Método Recomendado: Uvicorn con Reload

```powershell
# Activar entorno virtual primero
.\venv\Scripts\Activate.ps1

# Ejecutar la aplicación
python -m uvicorn app.main:app --reload
```

### Método Alternativo: Python Directo

```powershell
python app/main.py
```

### ✅ Verificar que Funciona

La aplicación estará disponible en:

- **🏠 Página principal**: http://localhost:8000
- **📚 Documentación Swagger**: http://localhost:8000/docs
- **📖 Documentación ReDoc**: http://localhost:8000/redoc
- **❤️ Health Check**: http://localhost:8000/api/v1/health

## 🧪 Testing y Uso de la API

### **1. 📚 Documentación Interactiva (Recomendado)**

Navega a `http://localhost:8000/docs` para:

- ✅ Ver todos los endpoints disponibles
- ✅ Probar cada endpoint directamente
- ✅ Ver ejemplos de JSON
- ✅ Configurar autenticación JWT

### **2. 🔐 Autenticación JWT**

Para endpoints protegidos (POST):

1. En Swagger UI, hacer clic en **"Authorize"**
2. Introducir: token designado
3. Hacer clic en **"Authorize"**

### **3. 📊 Endpoints Disponibles**

| Método   | Endpoint                | Descripción                  | Protegido |
| -------- | ----------------------- | ---------------------------- | --------- |
| `GET`    | `/api/v1/products`      | Listar todos los productos   | ❌        |
| `GET`    | `/api/v1/products/{id}` | Obtener producto por ID      | ❌        |
| `POST`   | `/api/v1/products`      | Crear nuevo producto         | ✅ JWT    |
| `PUT`    | `/api/v1/products/{id}` | Actualizar producto completo | ❌        |
| `PATCH`  | `/api/v1/products/{id}` | Actualizar producto parcial  | ❌        |
| `DELETE` | `/api/v1/products/{id}` | Eliminar producto            | ❌        |

### **4. 🔀 GraphQL**

Accede a GraphQL Playground en: `http://localhost:8000/graphql`

**Ejemplo Query:**

```graphql
query GetProducts {
  products {
    id
    nombre
    precio
    categoria
  }
}
```

**Ejemplo Mutation:**

```graphql
mutation CreateProduct($input: ProductInput!) {
  createProduct(input: $input) {
    id
    nombre
    precio
  }
}
```

### **5. 💻 Herramientas Externas**

- **Postman**: Importar colección desde `/docs`
- **Insomnia**: Soporte nativo para OpenAPI
- **curl**: Ejemplos en la documentación

## � Base de Datos

### **📊 Estructura de Datos (3 Niveles)**

```json
{
  "id": 1, // Nivel 1: Información básica
  "nombre": "MacBook Air M2 13' 256GB",
  "precio": 1299990.0,
  "categoria": "Laptops",
  "marca": "Apple",
  "stock": 15,
  "especificaciones": [
    // Nivel 2: Grupos de especificaciones
    {
      "grupo": "Procesador",
      "detalles": [
        // Nivel 3: Detalles específicos
        { "atributo": "Chip", "valor": "Apple M2 de 8 núcleos" },
        { "atributo": "GPU", "valor": "8 núcleos integrados" }
      ]
    }
  ]
}
```

## 🤝 Equipo de Desarrollo

- **Pablo Antivil**
- **Sion Arancibia**

## 📚 Recursos y Referencias

### **📖 Documentación Oficial**

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Strawberry GraphQL](https://strawberry.rocks/)

### **🎓 Material del Curso**

- [Guía Teórica REST](./README-Instrucciones.md) - Conceptos fundamentales
- [Principios REST](https://restfulapi.net/) - Referencia externa

### **🔧 Herramientas Recomendadas**

- **VS Code** - Editor con extensiones FastAPI
- **Postman** - Testing de APIs
- **Git** - Control de versiones

---

## 📄 Licencia

Este proyecto fue desarrollado con fines educativos para el curso **INFO1189** de la **Universidad Católica de Temuco**.

---

**🚀 REST API - Desarrollado con FastAPI para INFO1189**
