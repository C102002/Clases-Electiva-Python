# Crea una clase base llamada Animal con atributos name y sound. Luego, crea subclases
# para tres (3) animales específicos (por ejemplo, Perro, Gato, Loro). Cada subclase debe
# sobrescribir el atributo sound y proporcionar un sonido específico para ese animal.
# Copie el código con su respuesta en el lugar indiccado

class Animal:
    def __init__(self,name:str="no name", sound:str="no sound"):
        self.name=name
        self.sound=sound
        pass

class Perro(Animal):
    def __init__(self, name = "no name", sound = "no sound"):
        super().__init__(name, "guao guao")


class Gato(Animal):
    def __init__(self, name = "no name", sound = "no sound"):
        super().__init__(name, "miao miao")


class Loro(Animal):
    def __init__(self, name = "no name", sound = "no sound"):
        super().__init__(name, "bella rrrrr bella")
        
loro=Loro()
print(f"loro:{loro.sound}")
gato=Gato()
print(f"gato:{gato.sound}")
perro=Perro()
print(f"perro:{perro.sound}")
