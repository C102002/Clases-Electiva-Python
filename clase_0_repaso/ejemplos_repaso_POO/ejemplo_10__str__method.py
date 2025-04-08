class Jester:
    def laugh(self):
        return print("laugh() called")
    
    # __str__ es un metodo especial que se llama cuando se imprime el objeto es como el toString de Java
    def __str__(self):
        return 'Este es un objeto de la clase Jester'

if __name__ == "__main__": 
    obj = Jester()
    print(obj)