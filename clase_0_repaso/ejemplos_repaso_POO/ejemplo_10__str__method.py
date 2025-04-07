class Jester:
    def laugh(self):
        return print("laugh() called")

    def __str__(self):
        return 'Este es un objeto de la clase Jester'

if __name__ == "__main__": 
    obj = Jester()
    print(obj)