"""
A continuación se pide implementar una parte de una aplicación de gestión de empleados usando FastAPI, Pydantic y los principios de DDD.
Deberá crear un modelo de Dominio para un Employee , implementar un Repository (con sus métodos add_employee() 
y get_employee() ), para gestionar los pedidos y exponeer un endpoint de la API para crear un nuevo empleado. 

Requisitos: 

1. Modelo de Dominio: Crea un Value Object llamado Address con los atributos street , city , y zipcode . Crea una Entity llamada Employee que contenga un employee_id , name y una Address . Crea un Aggregate Root llamado EmployeeAgregate que tenga un employee_id y un Employee . 

2. Repository: Implementa una clase EmployeeRepository que permita agregar y recuperar empleados. 3. API: Crea un endpoint en FastAPI que permita crear un nuevo pedido. Este endpoint debe aceptar un objeto Employee y devolver ponmelo como comentarios para python

3. API:
Crea un endpoint en FastAPI que permita crear un nuevo pedido.
Este endpoint debe aceptar un objeto Employee y devolver
el employee_id del empleado creado.

"""

from abc import ABC, abstractmethod
import random
from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
app = FastAPI()
# Value Object
# street , city , y zipcode
class Address(BaseModel):
    street: str= Field(max_length=16)
    city: str = Field(min_length=3)
    zipcode: int = Field(gt=0)  
        
class EmployeeName(BaseModel):
    name:str =Field(max_length=10)

# Entity
# Crea una Entity llamada Employee que contenga un employee_id , name y una Address
class Employee(BaseModel):
    employee_id:int= Field(None,gt=0)
    name:str =Field(max_length=10)
    address:Address

# Aggregate Root
# rea un Aggregate Root llamado EmployeeAgregate que tenga un employee_id y un Employee
class EmployeeAggregate(BaseModel):
    employee_id:int=Field(gt=0)
    employee:Employee
    
# Repository
# agregar y recuperar empleados
class EmployeeRepository(ABC):
    employees:List[Employee]
    
    def __init__(self):
        self.employees = []
        pass
    @abstractmethod
    async def add_employee(employee:EmployeeAggregate):
        pass
    @abstractmethod
    async def get_all_employees(self) -> List[EmployeeAggregate]:
        pass
    
class PostgressEmployeeRepository(EmployeeRepository):
    
    def __init__(self):
        super().__init__()
    
    async def add_employee(self,employee:EmployeeAggregate):
        
        self.employees.append(
            Employee(
                employee_id=employee.employee_id,
                name=employee.employee.name,
                address=employee.employee.address
            )
        )
        
    async def get_all_employees(self) -> List[EmployeeAggregate]:
        employees_return:List[EmployeeAggregate]=[]
        for employee_infra in self.employees:
            employees_return.append(
                EmployeeAggregate(
                    employee_id=employee_infra.employee_id,
                    employee=employee_infra
                )
            )
        return employees_return
    

employee_repository = PostgressEmployeeRepository()

@app.post("/employees")
async def create_employee(items: Employee):
    if items.employee_id is None:
        items.employee_id=int(random.uniform(1,1000))
    
    employee_agregate=EmployeeAggregate(
        employee_id=items.employee_id,
        employee=items
    )
    response=await employee_repository.add_employee(employee_agregate)
    
    return{"employee_id":items.employee_id,
           "message":"employee created sucsesfully"}

     

@app.get("/employees")
async def get_all_employee():
    employees = await employee_repository.get_all_employees() 
    return employees    