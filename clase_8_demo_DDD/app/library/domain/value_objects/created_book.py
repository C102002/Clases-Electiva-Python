from pydantic import BaseModel, Field

class BookCreate(BaseModel):
    title: str
    author: str
    isbn: str = Field(min_length=10, max_length=13)