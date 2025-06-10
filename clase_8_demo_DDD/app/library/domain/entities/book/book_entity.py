from pydantic import BaseModel, Field, ConfigDict

class Book(BaseModel):
    id: int
    title: str
    author: str
    isbn: str = Field(min_length=10, max_length=13)

    model_config = ConfigDict(
        from_attributes=True
    )