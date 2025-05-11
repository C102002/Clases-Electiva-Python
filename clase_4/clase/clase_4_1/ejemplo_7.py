import time
from pydantic import BaseModel
from datetime import datetime

class Blog(BaseModel):
    title: str 
    created_at: datetime = datetime.now()
    is_active: bool

print(Blog(title="Our First Blog",is_active=True))

time.sleep(5)

print(Blog(title="Our Second Blog",is_active=True))