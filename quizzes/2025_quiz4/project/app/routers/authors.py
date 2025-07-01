from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.db import get_session
from app.models import Author, AuthorCreate, AuthorRead, BookRead, Book

# Crea un APIRouter
router = APIRouter(
    prefix="/authors", # Define un prefijo común para todas las rutas en este router
    tags=["Authors"],  # Agrupa las rutas en la documentación de Swagger UI
)

@router.post("/", response_model=AuthorRead)
async def create_author(author: AuthorCreate, session: AsyncSession = Depends(get_session)):
    db_author = Author.model_validate(author) # Se usa .model_validate para convertir Pydantic a SQLModel
    session.add(db_author)
    await session.commit()
    await session.refresh(db_author)
    return db_author

@router.get("/", response_model=list[AuthorRead])
async def get_authors(session: AsyncSession = Depends(get_session)):
    result = await session.exec(select(Author))
    authors = result.all()
    return authors

@router.get("/{author_id}", response_model=AuthorRead)
async def get_author(author_id: int, session: AsyncSession = Depends(get_session)):
    author = await session.get(Author, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author

@router.get("/authors/{author_id}/books", response_model=list[BookRead])
async def get_author(author_id: int, session: AsyncSession = Depends(get_session)):
    result = await session.exec(select(Book))
    book = result.all()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book