from datetime import datetime
from typing import List
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str = 'John Doe'
    signup_ts: datetime | None = None
    friends: List[int] = []


external_data = {
    'id': 123,
    'signup_ts': '2024-04-01 12:22',
    'friends': [1, '2', b'3'],
}

user = User(**external_data)

# Se puede tener acceso a los atributos del 
# objeto de la manera normal
print(user.id)
print(user.name)
print(user.signup_ts)
print(user.friends)

# o como un modelo json()
print(user.model_dump_json())

