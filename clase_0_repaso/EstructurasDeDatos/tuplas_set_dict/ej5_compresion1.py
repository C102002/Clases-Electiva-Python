# una compresion sencilla:

lista = [x for x in range(10, 20)]
listx = list(range(10, 20))
print(lista)
print(listx)

# otro ejemplo
listb = [x**2 + x + 2 for x in range(7)] 
print(listb)

# un ejemplo más elaborado
# es como una función lambda
# pero en una sola línea
# la función lambda es una función anónima primero se hace el rango de 0 a 30
# y se le aplica la función lambda
# lambda x: x**0.5 + 3*x
# osea 0**0.5 + 3*0, 1**0.5 + 3*1, 2**0.5 + 3*2, etc
listc = [x**0.5 + 3*x for x in range(0, 30, 5)]
print(listc)

# usando if como filtro
listd = [x + 5 for x in range(0, 30) if x%3 == 0]
print(listd)

