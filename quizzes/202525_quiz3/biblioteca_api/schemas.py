from pydantic import BaseModel, Field

class Book(BaseModel):
    title: str
    author: str
    year: int = Field(..., gt=0)