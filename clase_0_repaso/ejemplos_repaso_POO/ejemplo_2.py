class C: 

    # atributo de clase
    counter = 0
    
    def __init__(self): 
        type(self).counter += 1

    # sobreescritura de la función del
    def __del__(self):
        type(self).counter -= 1

if __name__ == "__main__":
    x = C()
    print("Número de instancia (x): " + str(C.counter))
    y = C()
    print("Número de instancia (y) : " + str(C.counter))
    del x
    print("Número de instancia: (x)" + str(C.counter))
    del y
    print("Número de instancia: (y)" + str(C.counter))
  
    print()
    z = C()
    z.counter = 10
    print("Número de instancia: (z)" + str(C.counter))
    print(z.counter)
    b = C()
    print("Número de instancia: (b)" + str(C.counter))
    print(z.counter)
  