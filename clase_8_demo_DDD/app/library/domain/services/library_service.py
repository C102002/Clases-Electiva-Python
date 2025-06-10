from app.library.domain.repositories.i_book_repository import IBookRepository
from app.library.domain.value_objects.created_book import BookCreate
from app.library.domain.entities.book.book_entity import Book

class LibraryService:
    def __init__(self, repository: IBookRepository):
        self.repository = repository

    def get_all_books(self) -> list[Book]:
        return self.repository.get_all_books()

    def add_book(self, book: BookCreate) -> Book:
        return self.repository.add_book(book)