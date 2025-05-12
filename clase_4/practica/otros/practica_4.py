"""
Cree un aplicación simple con FastAPI que tenga cuatro endpoint tres GET y un
POST. En este caso va a usar un schema Pydantic llamado Usuario, elcual va
tener un id(int), un nombre completo(str), usuario(str), email(Pydantic.Email) y password (str). Los datos se guardaran en una listaque usará como base de datos.
El POST, incluirá un Usuario en la lista
El primer GET estará en la base de la aplicación e indicará unmensaje: "Bienvenidos a la aplicación de ejemplo"
El segundo GET mostrará todos los usuarios, en el path /users/
El segundo GET mostrará un usuario por su ID, en el path /users/{id}"""

from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel,EmailStr

app = FastAPI()


# usando un schema Pydantic
class Usuario(BaseModel):
    id: int
    nombre_completo: str
    usuario: str
    email:EmailStr
    password:str

users:list[Usuario]=list()


@app.get("/")
def read_root():
    return "Bienvenidos a la aplicación de ejemplo"


@app.get("/users")
def read_item():
    return users

@app.post("/users/")
def create_user(user: Usuario):
    users.append(user)


# demo del uso del schema Pydantic
@app.get("/users/{id}")
def get_user_by_id(id: int):
    for i in users:
        if i.id==id:
            return i
    raise ValueError(f"elemento con el id {id} no se encontro")