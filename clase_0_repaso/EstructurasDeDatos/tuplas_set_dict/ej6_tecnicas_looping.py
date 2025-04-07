"""
# recorriendo un diccionario
dict = {1:2, 2:3, 3:4, 4:5, 5:6}
for k,v in dict.items():
    print(f'clave: {k}, valor: {v}')

print(30*'-')


# usando enumerate para obtener el indice y el valor de una lista
lista = [23, 45, 23, 67, 4, 8, 1, 65]
for elem in enumerate(lista):
    print(elem)
    # descomposición de tupla
    idx, valor = elem
    print(f'indice {idx} , valor {valor}')

print(30*'-')


# usando zip para recorrer dos listas de forma simultánea
listb = [x**2 for x in range(10)]
listc = [x**3 for x in range(10)]
print(listb)
print(listc)

for x in zip(listb, listc):
    print(x)

print(30*'-')

lista = [23, 45, 23, 67, 4, 8, 1, 65]
# recorriendo una lista de forma invertida:
for i in reversed(lista):
    print(i)

print(30*'-')


# recorriendo la lista de forma ordenada:
print(lista, end=" ")
print()
# de menor a mayor
for i in sorted(lista):
    print(i, end=' ')

print()

"""
lista = [23, 45, 23, 67, 4, 8, 1, 65]
# de mayor a menor
for i in sorted(lista, reverse= True):
    print(i, end=' ')

print()

listd = ['string1', 'casa', 'xilofono', 'burro', 'ratón']
print(listd)
# de menor a mayor
for i in sorted(listd):
    print(i, end=' ')

print()

# de mayor a menor
for i in sorted(listd, reverse= True):
    print(i, end=' ')

print()
