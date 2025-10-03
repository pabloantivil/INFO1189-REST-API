# Aquí se definirán las funciones para interactuar con la base de datos
# Por simplicidad, usaremos una lista en memoria como "base de datos"
db = [
    {
        "id": 1,
        "title": "El principe",
        "date": "10/10/2020",
        "price": 2000,
        "authors": [{
            "id": 1,
            "name": "sion",
            "age": 20,
        }],
        "category": {
            "id": 1,
            "name": "terror",
            "subcategories": [{
                "id": 1,
                "name": "terror arcaico" 
            }]
        }

    },

    {
        "id": 2,
        "title": "El sayayin",
        "date": "10/10/2020",
        "price": 2000,
        "authors": [{
            "id": 1,
            "name": "sion",
            "age": 20,
        }],
        "category": {
            "id": 1,
            "name": "terror",
            "subcategories": [{
                "id": 2,
                "name": "terror suspenso" 
            }]
        }

    },

    {
        "id": 3,
        "title": "El retorno",
        "date": "10/10/2021",
        "price": 2000,
        "authors": [{
            "id": 1,
            "name": "pablo",
            "age": 20,
        }],
        "category": {
            "id": 2,
            "name": "suspenso",
            "subcategories": [{
                "id": 3,
                "name": "terror suspenso" 
            }]
        }

    }
]

def get_books():
    return db

def get_books_by_id(id: int):
    in_db = False    
    for book in db:  
        if book.get("id") == id:
            in_db = True
            return db[book.get("id")]
        
    if in_db == False:
        return "no existe este id"

def create_book(data):
    db.append(data)



    