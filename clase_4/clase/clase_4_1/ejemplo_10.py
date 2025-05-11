# serilaización - deserialización
import json

from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str

# Crear un objeto de usuario
user = User(id=1, name="John Doe", email="johndoe@example.com")

# Serializar el objeto a un diccionario
user_dict = user.model_dump()
print(f"el objeto serializado a un dict: {user_dict}")
print()  

# Serializar el objeto a JSON

user_json = json.dumps(user_dict)
print(f"el objeto serializado a json {user_json}")
print()  

# Deserializar un diccionario a un objeto de usuario
new_user_data = {'id': 2, 'name': 'Jane Smith', 'email': 'janesmith@example.com'}
new_user = User.model_validate(new_user_data)
print(f"el diccionario deserializado a un obj: {new_user}")