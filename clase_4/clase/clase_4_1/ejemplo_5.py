from pydantic import BaseModel
from typing import List

class Comment(BaseModel):
    text: str | None = None

class Blog(BaseModel):
    title: str 
    comment: List[Comment] | None
    is_active: bool
    
# Sub-objetos de Pydantic anidados en este caos blog y comment
my_blog = Blog(title="Our First Blog",comment=[{'text':'My comment'},{'text':'Your comment'},],is_active=True)

# Otra cosa "buena" de Pydantic es que puedes usar el modelo como automatizador de getter y setter
print(my_blog)
print()
print(my_blog.model_dump_json())