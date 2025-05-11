from pydantic import BaseModel, Field

class Blog(BaseModel):
    title: str = Field(...,min_length=5)
    is_active: bool

Blog(title="hi",is_active=False)