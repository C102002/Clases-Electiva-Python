from datetime import datetime
from typing import List
from pydantic import BaseModel
from pydantic import ValidationError

class User(BaseModel):
    id: int
    name: str = 'John Doe'
    signup_ts: datetime | None = None
    friends: List[int] = []

# Datos de entrada errados 
# o un dato requerido no está presente

external_data = {
    'id': 'not an int', #Esta esperando un int
    'tastes': {}, # Esta esperando un str pero no esta y tates no existe asi que lo omite
}

external_data_1 = {
    'id': 2, #Esta esperando un int
    'tastes': {}, # Esta esperando un str pero no esta y tates no existe asi que lo omite
}

try:
    user = User(**external_data_1)
    print(f"user: {user.model_dump_json()}")
except ValidationError as e:
    print(e.errors())
