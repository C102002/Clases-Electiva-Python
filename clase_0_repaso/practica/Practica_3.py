from abc import ABC, abstractmethod

# Practica 3: Factory Method y Abstract Factory
class Animal(ABC):    
    
    def __init__(self, name=None):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
        
    # Factory method
    @abstractmethod
    @staticmethod
    def create_vacio():
        return Animal()
    
class Mamifero(Animal):
    
    def __init__(self, name=None):
        super().__init__(name)

    def set_name(self, name):
        return super().set_name(f"el nombre es {name} y es un mamifero")
        
if __name__ == "__main__":
    a= Animal()
    print(f"el animal es {a.get_name()} ")
    b: Mamifero= Mamifero.create_vacio()
    b.set_name("perro")
    print(f"el animal es {b.get_name()} ")