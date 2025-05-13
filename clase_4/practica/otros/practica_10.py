"""Crea una clase abstracta base llamada Animal con atributos name y sound.
Luego, crea subclases para tres (3) animales específicos (por ejemplo,Perro, Gato, Loro).
Cada subclase debe sobrescribir el atributo sound yproporcionar un sonido específico para ese animal. 
Copie el código consu respuesta en el lugar indiccado"""


# Practicando con clase abstracta


from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self,name:str,sound:str):
        self.name=name
        self.sound=sound
        super.__init__()
        pass
    def __str__(self):
        return f"name {self.name}, sound {self.sound}"
    
class Perro(Animal):
    def __init__(self, name):
        super().__init__(name, "guao guao")
        
class Gato(Animal):
    def __init__(self, name):
        super().__init__(name, "miao miao")
        
class Loro(Animal):
    def __init__(self, name):
        super().__init__(name, "lorito, lorito hola")
        
perro=Perro("perro")

gato=Gato("gato")

loro=Loro("loro")

print(f"perro:{perro}")
print(f"gato:{gato}")
print(f"loro:{loro}")