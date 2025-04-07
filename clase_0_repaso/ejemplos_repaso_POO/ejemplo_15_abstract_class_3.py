from abc import ABC, abstractmethod
 
class AbstractClassExample(ABC):
 
    def __init__(self, value):
        self.value = value
        super().__init__()
    
    @abstractmethod
    def do_something(self):
        print("estoy en el metodo abstracto de la clase abstracta")

class AnotherSubclass(AbstractClassExample):
    def do_something(self):
        super().do_something()
        print("Enriquecido en AnotherSubclass")
    

if __name__ == "__main__":
    x = AnotherSubclass(5)
    x.do_something()