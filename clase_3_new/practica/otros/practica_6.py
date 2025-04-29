# Modifique la funcionalidad para que sea realizada con una función generadora, luego
# con un ciclo iterativo generando la funcion

# Python 3: Fibonacci series up to n
def fib(n=0):
    i=0
    a, b = 0, 1
    while i < n:
         yield a
         a, b = b, a+b
         i=i+1

print(f"el valor de fibonnaci de 15 es:")

for i in fib(15):
    print(f"valor:{i}")