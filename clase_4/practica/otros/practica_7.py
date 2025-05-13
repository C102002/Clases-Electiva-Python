"""
Cree un aplicación simple con FastAPI que tenga cuatro endpoint tres GET y un POST. En este caso va a usar un schema Pydantyc 
llamado Empleado, el cual va tener un id(int), una nombre completo(str), cargo(str), sueldo(str) y departamento (Enum.Departamento), este ultimo
es un Enumerado que tendrá cuatro valores str:
Finanzas, RRHH, Producción y TRansporte. Los datos se guardaran en una lista que
usará como base de datos.


El POST, incluirá un Empleado en la lista
El primer GET estará en la base de la aplicación e indicará un mensaje: "Bienvenidos a
la aplicación de ejemplo"
El segundo GET mostrará todos los empleados, en el path /employees/
El segundo GET mostrará un empleado por su ID, en el path /employees/{id}
"""

from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum


app = FastAPI()

class Departamento(str,Enum):
    Finanzas="Finanzas", 
    RRHH="RRHH", 
    Producción="Producción",
    Transporte="Transporte"

# usando un schema Pydantic
class Empleado(BaseModel):
    id: int
    nombre_completo: str
    cargo: str
    sueldo:str
    departamento:Departamento

employees:list[Empleado]=list()


@app.get("/")
def read_root():
    return "Bienvenidos a la aplicación de ejemplo"


@app.get("/employees")
def read_item():
    return employees

@app.post("/employees/")
def create_user(user: Empleado):
    employees.append(user)


# demo del uso del schema Pydantic
@app.get("/employees/{id}")
def get_user_by_id(id: int):
    for i in employees:
        if i.id==id:
            return i
    raise ValueError(f"elemento con el id {id} no se encontro")