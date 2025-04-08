class Animal:    
    
    def __init__(self, name=None):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
        
    # Factory method
    @staticmethod
    def create_vacio():
        return Animal()
    
class Mamifero(Animal):
    
    def __init__(self, name=None):
        super().__init__(name)
        
if __name__ == "__main__":
    a= Animal()
    print(f"el animal es {a.get_name()} ")
    b= Mamifero.create_vacio()
    b.set_name("perro")
    print(f"el animal es {b.get_name()} ")