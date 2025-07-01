from fastapi import APIRouter, HTTPException

from db import fake_db
from schemas import Book

router = APIRouter()

@router.post("/")
def add_book(book: Book):
    fake_db.books.append(book)
    return {"message": "Libro añadido", "id": len(fake_db.books) - 1}

@router.get("/")
def list_books():
    return fake_db.books

@router.get("/{book_id}")
def get_book(book_id: int):
    if book_id >= len(fake_db.books) or book_id < 0:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return fake_db.books[book_id]