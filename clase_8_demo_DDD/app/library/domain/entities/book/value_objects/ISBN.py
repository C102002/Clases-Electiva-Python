from pydantic import BaseModel, Field

class ISBN(BaseModel):
    value: str = Field(min_length=10, max_length=13)