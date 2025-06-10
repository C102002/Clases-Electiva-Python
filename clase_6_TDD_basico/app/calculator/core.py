class Calculator:    
    def __init__(self, a: int | float = None, b: int | float = None) -> None:    
        self.a = a    
        self.b = b    
    
    def suma(self) -> int | float:    
        """    
        Suma dos números   
        return: la suma de dos números    
        """    
        return self.a + self.b    
    
    def resta(self) -> int | float:    
        """    
        Hace la resta de dos números    
        return: la diferencia de dos números    
        """    
        return self.a - self.b    
    
    def multiplica(self) -> int | float:    
        """    
        Multiplica dos números    
        return: el productpo de dos números
        """    
        return self.a * self.b    
    
    def divide(self) -> int | float:    
        """    
        Divide dos número
        return: el cuociente de dos números
        """    
        if self.b != 0:    
            return self.a / self.b    
        else:    
            raise ZeroDivisionError("Cannot divide by zero")    
    
    def cuadrado(self) -> int | float:    
        """    
        Calcula el cuadrado de un número    
        return: el cuadrado de un número        
        """    
        return self.a**2