"""
lista = list(range(10,100, 5))
print(lista)

for num in lista:
    print(num, end=" ")

respuesta = 's'
palabras = list()
while respuesta == 's':
    palabra = input('ingrese una palabra: ')
    palabras.append(palabra)

    respuesta = input('¿Desea continuar[s/n]')

print(palabras)


oracion = input('ingrese una oración:')
palabras = oracion.split(' ')
idx = 0
for p in palabras:
    print(f'Indice {idx}: {p}')
    idx += 1

print(type(palabras))
print(palabras)


lista = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
# elemento 0 de la lista
print(lista[0])

# elemento 1 de la lista 2
print(lista[2][1])

"""
numeros = input('ingrese una lista de numeros separados por espacio')
lista = numeros.split(' ')
suma = 0
for i in lista:
    print(i, end=' - ')
    suma += int(i)

print(f'la suma de la lista es {suma}')

