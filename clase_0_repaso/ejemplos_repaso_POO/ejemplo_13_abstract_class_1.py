from abc import ABC, abstractmethod
 
class AbstractClassExample(ABC):
 
    def __init__(self, value):
        self.value = value
        super().__init__()
    
    @abstractmethod
    def do_something(self):
        pass

class DoAdd42(AbstractClassExample):
    pass

if __name__ == "__main__":
    x = DoAdd42(4)