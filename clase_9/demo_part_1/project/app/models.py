from sqlmodel import SQLModel, Field


class BookBase(SQLModel):
    name: str
    author: str


class Book(BookBase, table=True):
    __tablename__ = "books"
    id: int = Field(default=None, nullable=False, primary_key=True)


class BookCreate(BookBase):
    pass
