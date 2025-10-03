from fastapi import APIRouter, Depends, HTTPException, Response
from typing import List
from app.models.schemas import Book
from app.services.database import get_books, get_books_by_id, create_book
#from app.utils.token import JWTBearer
from fastapi_cache.decorator import cache


# Crear el router
router = APIRouter()


@router.get("/books")
#@cache(expire=60)
async def get_book():
    return get_books()

@router.get("/books/{id}")
#@cache(expire=60)
async def get_book(id: int):
    return get_books_by_id(id)

@router.post("/books") # , dependencies=Depends(JWTBearer)
async def create_book(book: Book):
    return create_book(book)