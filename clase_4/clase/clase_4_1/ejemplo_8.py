import time
from pydantic import BaseModel, Field
from datetime import datetime

class Blog(BaseModel):
    title: str 
    created_at: datetime = Field(default_factory=datetime.now)
    is_active: bool

print(Blog(title="Our First Blog",is_active=True))

time.sleep(5)
# Ahora si, como usamos el default_factory, el created_at es diferente con el Field
print(Blog(title="Our Second Blog",is_active=True))