from datetime import datetime
from typing import List
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str = 'John Doe'
    signup_ts: datetime | None = None
    friends: List[int] = []

# Para crear  una instancia de  este modelo, se puede pasar
# un diccinario con los valores al constructor

external_data = {
    'id': 123,
    'signup_ts': '2024-10-09 12:22',
    'friends': [1, '2', b'3'],
}

user = User(**external_data)

print(user)
print(type(user))