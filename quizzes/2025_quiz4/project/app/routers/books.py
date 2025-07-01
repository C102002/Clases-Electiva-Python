from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.db import get_session
from app.models import Author, AuthorCreate, AuthorRead, BookRead, BookCreate, Book

# Crea un APIRouter
router = APIRouter(
    prefix="/books", # Define un prefijo común para todas las rutas en este router
    tags=["Books"],  # Agrupa las rutas en la documentación de Swagger UI
)

@router.post("/", response_model=BookRead)
async def create_book(book: BookCreate, session: AsyncSession = Depends(get_session)):
    db_book = Book.model_validate(book) # Se usa .model_validate para convertir Pydantic a SQLModel
    session.add(db_book)
    await session.commit()
    await session.refresh(db_book)
    return db_book

@router.get("/", response_model=list[BookRead])
async def get_books(session: AsyncSession = Depends(get_session)):
    result = await session.exec(select(Book))
    books = result.all()
    return books
