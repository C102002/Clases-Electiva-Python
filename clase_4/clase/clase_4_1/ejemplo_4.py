from pydantic import BaseModel
from enum import Enum

# Enums como los de JAVA o Ts
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

# Debe de dar error porque el lenguaje c++ no esta
try:
    blog_2 = Blog(title="My Second Blog",language="C++",is_active=True)
    print(blog_2)
except ValueError as e:
    print(e.errors())
    print(e.json())

blog3=Blog(title="My Third Blog",language=Languages.GO,is_active=True)
print(f"blog3: {blog3}")