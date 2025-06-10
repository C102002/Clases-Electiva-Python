from fastapi import APIRouter, Depends, HTTPException
from app.library.domain.services.library_service import LibraryService
from app.library.domain.value_objects.created_book import BookCreate
from app.library.domain.entities.book.book_entity import Book
from app.library.infrastructure.repositories.orm_book_repository import SQLAlchemyBookRepository


router = APIRouter()

async def get_library_service():
    repository = SQLAlchemyBookRepository()
    return LibraryService(repository)

@router.get("/books/", response_model=list[Book])
async def get_books(library_service: LibraryService = Depends(get_library_service)):
    return library_service.get_all_books()

@router.post("/books/", response_model=Book)
async def add_book(book: BookCreate, library_service: LibraryService = Depends(get_library_service)):
    return library_service.add_book(book)