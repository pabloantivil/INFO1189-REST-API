🏢 CONTEXTO EMPRESARIAL
Empresa: "TechLibrary Solutions" - Plataforma digital de gestión de libros

Situación: La empresa necesita desarrollar una API REST para gestionar su catálogo de libros digitales. Los clientes podrán consultar información de libros y los administradores podrán agregar nuevos títulos al catálogo.

📋 ESPECIFICACIONES TÉCNICAS A IMPLEMENTAR
🎯 ENDPOINT REQUERIDO:
Implementar ÚNICAMENTE el endpoint: POST /libros

📚 ESTRUCTURA DEL RECURSO "LIBRO" (JSON - máximo 3 niveles):
🔒 SEGURIDAD REQUERIDA:
El endpoint POST debe estar protegido con JWT
Token de autorización: Bearer secret123
Sin token válido → Error 401 Unauthorized

⚙️ TECNOLOGÍA:
FastAPI obligatorio
Puede usar código base existente y adaptarlo
O implementar desde cero

⏰ INSTRUCCIONES
Adaptar/crear su API para el contexto de TechLibrary
Implementar POST /libros con la estructura JSON especificada
Proteger con JWT (Bearer secret123)