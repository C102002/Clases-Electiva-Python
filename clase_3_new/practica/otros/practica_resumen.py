from typing import List

class MiEstructura:

    def __init__(self, lista: List):
        self.lista: List = lista

    def __len__(self) -> int:
        return len(self.lista)
    
x = MiEstructura([1, 2, 3, 4, 5])

# print(len(x))


def pares_hasta(x: int):
    n = 2
    while n <= x:
        yield n
        n += 2

y = pares_hasta(20)

# for par in y:
#     print(par)

def potencias(numero: int, exponente: int):
    n = 1
    while n <= exponente:
        yield numero ** n
        n += 1

z = potencias(2, 5)

# for potencia in z:
#     print(potencia)

def fib():
    a,b = 0,1
    while True:
        yield a
        a,b = b, a+b

w = fib()
i = 1

# while i <= 15:
#     print(next(w))
#     i += 1

import math
import time

def calcula_tiempo(func):
    def wrapper(num):
        inicio = time.time()
        func(num)
        fin = time.time()
        print(f"tiempo de ejecucion: {fin - inicio}")
    return wrapper

@calcula_tiempo
def factorial(num):
    time.sleep(2)
    print(math.factorial(num))

factorial(num=10)