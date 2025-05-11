from pydantic import BaseModel
from enum import Enum

class Languages(str,Enum):
    PY = "Python"
    JAVA = "Java"
    GO = "Go"

class Blog(BaseModel):
    title: str 
    language : Languages = Languages.PY
    is_active: bool
    


blog1 = Blog(title="My First Blog",language="Java",is_active=True)
print(blog1)

blog_2 = Blog(title="My Second Blog",language="C++",is_active=True)
print(blog_2)