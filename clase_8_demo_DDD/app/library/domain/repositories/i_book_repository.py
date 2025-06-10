from abc import ABC, abstractmethod
from typing import List

from app.library.domain.value_objects.created_book import BookCreate
from app.library.domain.entities.book.book_entity import Book


class IBookRepository(ABC):

    @abstractmethod
    def get_all_books(self) -> None | List[Book]:
        pass

    @abstractmethod
    def add_book(self, book: BookCreate) -> Book:
        pass
