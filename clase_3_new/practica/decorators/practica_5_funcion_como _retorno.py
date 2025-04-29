
def hello_function():
    def say_hi():
        return "Hi"
    return say_hi

hello = hello_function()

print(hello()) # imprime Hi
print() # espacio
print(hello) # imprime el objeto que es la funcion


