"""
Cree una clase base llamada Employee con atributos name, employee_idy salary. Luego, cree subclases para diferentes tipos de empleados (porejemplo, Gerente, Desarrollador, Vendedor). Cada subclase debe teneratributos y métodos adicionales específicos para su rol.

Recuerde sobreescribir el método __str__() para mostrar surepresentación.

A contininuación instancie objetos de tipo Gerente, Desarrollador y otrode tipo Vendedor, e imprima sus atributos por la pantalla.

Copie su código y péguelo en el lugar indicado. Revise que la indentaciónquedó bien configurada.

"""

class Employee:
    def __init__(self,name, employee_id, salary):
        self.name=name
        self.employee_id=employee_id
        self.salary=salary
        pass
    def __str__(self):
        return f"name:{self.name}, employee_id:{self.employee_id} , salary:{self.salary}"


class Gerernte(Employee):
    def __init__(self, name, employee_id, salary,lider):
        self.lider=lider
        super().__init__(name, employee_id, salary)
    def __str__(self):
        return super().__str__()+f" lider: {self.lider}"


class Desarrollador(Employee):
    def __init__(self, name, employee_id, salary,lenguaje):
        self.lenguaje=lenguaje
        super().__init__(name, employee_id, salary)
    def __str__(self):
        return super().__str__()+f" lenguaje: {self.lenguaje}"

class Vendedor(Employee):
    def __init__(self, name, employee_id, salary,area):
        self.area=area
        super().__init__(name, employee_id, salary)
    def __str__(self):
        return super().__str__()+f" area: {self.area}"
    

gerente=Gerernte("pepe","1","500",True)
vendedor=Vendedor("jose","2","200","maiquetia")
desarrollador=Desarrollador("pepe","1","500","C++")

print(f"gerente: {gerente}")
print(f"vendedor: {vendedor}")
print(f"desarrollador: {desarrollador}")

