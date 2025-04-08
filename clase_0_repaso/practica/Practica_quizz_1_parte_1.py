# Pregunta 1
# Crea una clase base llamada Animal con atributos name y sound.Luego, crea subclases para tres (3) animales específicos (por ejemplo,Perro, Gato, Loro). Cada subclase debe sobrescribir el atributo sound yproporcionar un sonido específico para ese animal. Copie el código consu respuesta en el lugar indiccado

class Animal:
    def __init__(self,name=None, sound=None):
        self.__name=name
        self.__sound=sound
        pass
    def get_name(self):
        return self.__name
    def get_sound(self):
        return self.__sound

class Perro(Animal):
    def __init__(self, name=None, sound="guau"):
        super().__init__(name, sound)
        pass

class Gato(Animal):
    def __init__(self, name=None, sound="miaw"):
        super().__init__(name, sound)
        
if __name__ == "__main__":
    a= Animal()
    print(f"el animal suena {a.get_sound()} ")
    b= Perro()
    print(f"el animal suena {b.get_sound()} ")
    c= Gato()
    print(f"el animal suena {c.get_sound()} ")