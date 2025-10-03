from pydantic import BaseModel
from typing import List

class Author(BaseModel):
    id: int
    name: str
    age: int

class SubCategory(BaseModel):
    id: int
    name: str

class Category(BaseModel):
    id: int
    name: str
    subcategories: List[SubCategory]
    
class Book(BaseModel):
    id: int
    title: str
    date: str
    price: int
    authors: List[Author] 
    category: Category



