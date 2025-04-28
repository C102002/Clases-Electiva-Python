class PowTwo:
    def __init__(self, max=0):
        self.n = 0
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration

        resultado = 2 ** self.n
        self.n += 1
        return resultado
    

def powTwoGen(max=0):
    n = 0
    while n < max:
        print(f"valor de n antes:{n}")
        yield 2 ** n
        n += 1
        print(f"valor de n despues:{n}")
        
        
# Haciendolo al estilo "python"
def naturalNumberGen(max=0):
    n = 0
    while n < max:
        yield n
        n += 1
    


print("usando iterators: ")
powtwo1 = PowTwo(5)
powtwo1_iter = iter(powtwo1)

while True:
    try:
        print(next(powtwo1_iter))
    except StopIteration:
        print("concluyo el iterador powtwo1_iter")
        break

print()
# OJO: Esta imrpimiendo 25 veces el caracter (-)
print(25*"-")
print()

print("usando generadores: ")
for value in powTwoGen(5):
    print(value)
    
print("usando generadores con una funcion normal: ")
for value in naturalNumberGen(5):
    print(value)



