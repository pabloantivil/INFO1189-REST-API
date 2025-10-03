# Aquí se definirán las funciones para interactuar con la base de datos
# Por simplicidad, usaremos una lista en memoria como "base de datos"

db = [
    {
        "id": 1,
        "titulo": "Nombre de libro",
        "precio": 25000,
        "detalles": [
            {
            "categoria": "Investigacion",
            "informacion": [
                {"campo": "nombre", "valor": "Roberto Martinez"},
                {"campo": "nacionalidad", "valor": "Estados Unidos"}
                ]
            }
        ]
    },
    {
        "id": 2,
        "titulo": "Nombre de libro",
        "precio": 28000,
        "detalles": [
            {
            "categoria": "Editorial",
            "informacion": [
                {"campo": "nombre", "valor": "Cristian Morales"},
                {"campo": "nacionalidad", "valor": "Argentina"}
                ]
            }
        ]
    },
]
