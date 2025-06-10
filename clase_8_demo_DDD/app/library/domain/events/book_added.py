from pydantic import BaseModel


class BookAddedEvent(BaseModel):
    book_id: int