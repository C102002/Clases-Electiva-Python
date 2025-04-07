# una compresion sencilla:

lista = [x for x in range(10, 20)]
listx = list(range(10, 20))
print(lista)
print(listx)

# otro ejemplo
listb = [x**2 + x + 2 for x in range(7)] 
print(listb)

# un ejemplo más elaborado
listc = [x**0.5 + 3*x for x in range(0, 30, 5)]
print(listc)

# usando if como filtro
listd = [x + 5 for x in range(0, 30) if x%3 == 0]
print(listd)

