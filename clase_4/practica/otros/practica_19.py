"""

Cree una clase llamada Persona con los siguientes atributos: nombre, fecha de nacimiento (como un string) y cédula de identidad. Luego cree dos clases que herenden de Persona:

1. una llamada Estudiante, con un atributo adicional denominado carrera, para indicar que carrera cursa

2. otra llamada Profesor, con un atributo adicional denominado asignatura, para indicar la materia que dicta.

En ambos casos recuerde sobreescribir el método __str__() para mostrar su representación.

A contininuación instancie dos objetos uno de tipo Estudiante y otro de tipo Profesor, e imprima sus atributos por la pantalla.

"""

class Persona:    
    def __init__(self,nombre, fecha_de_nacimiento, cedula):
        self.nombre=nombre
        self.fecha_de_nacimiento=fecha_de_nacimiento
        self.cedula=cedula
        pass
    def __str__(self):
        return f"nombre: {self.nombre}, fecha_de_nacimiento: {self.fecha_de_nacimiento}, cedula:{self.cedula}"

class Estudiante(Persona):
    def __init__(self, nombre, fecha_de_nacimiento, cedula,carrera):
        self.carrera=carrera
        super().__init__(nombre, fecha_de_nacimiento, cedula)
        
    def __str__(self):
        return super().__str__()+f"carrera:{self.carrera}"
    
class Profesor(Persona):
    def __init__(self, nombre, fecha_de_nacimiento, cedula,asignatura):
        self.asignatura=asignatura
        super().__init__(nombre, fecha_de_nacimiento, cedula)
        
    def __str__(self):
        return super().__str__()+f"asignatura:{self.asignatura}"
    
estudiante=Estudiante("pepe","24-10-2002","12345678","ingeniero informatico")
profesor=Profesor("maria","4-10-1989","12345679","mate discretas")

print(f"estudiante:{estudiante}")
print(f"profesor:{profesor}")

