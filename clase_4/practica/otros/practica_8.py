"""Crea una clase base llamada Animal con atributos name y sound.
Luego, crea subclases para tres (3) animales específicos (por ejemplo,Perro, Gato, Loro).
Cada subclase debe sobrescribir el atributo sound yproporcionar un sonido específico para ese animal. 
Copie el código consu respuesta en el lugar indiccado"""


class Animal:
    def __init__(self,name:str,sound:str):
        self.name=name
        self.sound=sound
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