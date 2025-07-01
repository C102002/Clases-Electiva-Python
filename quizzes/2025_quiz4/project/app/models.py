from sqlmodel import SQLModel, Field


class AuthorBase(SQLModel):
    first_name: str
    last_name: str
    nationality: str | None = None


class Author(AuthorBase, table=True):
    __tablename__ = "authors"
    id: int = Field(default=None, nullable=False, primary_key=True)


class AuthorCreate(AuthorBase):
    pass

class AuthorRead(AuthorBase):
    id: int


class BookBase(SQLModel):
    title: str
    year: int
    author_id: int = Field(foreign_key="authors.id", nullable=False)


class Book(BookBase, table=True):
    __tablename__ = "books"
    id: int = Field(default=None, nullable=False, primary_key=True)


class BookCreate(BookBase):
    pass

class BookRead(BookBase):
    id: int
