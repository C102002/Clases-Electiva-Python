from typing import List

from app.library.domain.entities import Book


class Library:
    def __init__(self) -> None:
        self.books: List[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)