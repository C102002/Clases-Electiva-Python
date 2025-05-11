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
    'id': 'not an int',
    'tastes': {},
}

try:
    user = User(**external_data)
except ValidationError as e:
    print(e.errors())
