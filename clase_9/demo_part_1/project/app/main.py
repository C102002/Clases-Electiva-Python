from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from sqlmodel import select, Session

from app.db import get_session, init_db
from app.models import Book, BookCreate


app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/ping")
def pong():
    return {"ping": "pong!"}


@app.get("/books", response_model=list[Book])
def get_books(session: Session = Depends(get_session)):
    result = session.exec(select(Book))
    books = result.all()
    return [Book(name=book.name, author=book.author, id=book.id) for book in books]


@app.post("/books")
def add_book(book: BookCreate, session: Session = Depends(get_session)):
    book = Book(name=book.name, author=book.author)
    session.add(book)
    session.commit()
    session.refresh(book)
    return book
