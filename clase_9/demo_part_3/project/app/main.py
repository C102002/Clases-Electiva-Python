from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.db import get_session, init_db
from app.models import Book, BookCreate


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     print("iniciando database")
#     await init_db()
#     yield
#     print("finallizando aplicación")

app = FastAPI()

# @app.on_event("startup")
# def on_startup():
#     init_db()


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


@app.get("/books", response_model=list[Book])
async def get_books(session: AsyncSession = Depends(get_session)):
    result = await session.exec(select(Book))
    books = result.all()
    return [Book(name=book.name, author=book.author, year=book.year, id=book.id) for book in books]


@app.post("/books")
async def add_book(book: BookCreate, session: AsyncSession = Depends(get_session)):
    book = Book(name=book.name, author=book.author, year=book.year)
    session.add(book)
    await session.commit()
    await session.refresh(book)
    return book
