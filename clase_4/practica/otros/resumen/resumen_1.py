from fastapi import FastAPI
from pydantic import BaseModel, Field
from enum import Enum

app = FastAPI()

class Departamento(str, Enum):
    FINANZAS = "Finanzas"
    RRHH = "RRHH"
    PRODUCCION = "Producción"
    TRANSPORTE = "Transporte"

class Empleado(BaseModel):
    id: int = Field(...)
    nombre_completo: str = Field(...)
    cargo: str = Field(...)
    sueldo: str = Field(...)
    departamento: Departamento = Field(...)

datos = []

@app.get("/")
def endpoint1():
    return "Bienvenidos a la aplicacion de ejemplo"

@app.get("/employees")
def endpoint2():
    return datos

@app.get("/employees/{id}")
def endpoint3(id: int):
    
    for empleado in datos:
        if empleado.id == id:
            return empleado
    
    return {"error": "Empleado no encontrado"}

@app.post("/")
def endpoint4(empleado: Empleado):
    datos.append(empleado)