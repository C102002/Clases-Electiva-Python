# haciendo un loopin en un diccionario para obtener la clave y el valor
dic1 = {'a': 123, 'b': 456, 'c': 234, 'd': 567}

dic1['e'] = 4564

for k,v in dic1.items():
    print(f'la clave es: {k} y el valor es {v}')

print(2*'\n')

# para obtener el indice en una secuencia y su valos se usa enumerate()
sec1 = ['a', 'b', 'c', 'd', 'e', 'f']
for idx, value in enumerate(sec1):
    print(f'El índice es {idx} y el valor es {value}')

print(2*'\n')

# usando zip para una iteracion paralela
numeros = [1, 2, 3, 4, 5, 6]
letras = ['a', 'b', 'c']

agrupado = list(zip(numeros, letras))
print(agrupado)

print(2*'\n')

# hacer un loop en forma reversa
sec2 = ['a', 'b', 'c', 'd', 'e', 'f']

print(sec2)
print(list(reversed(sec2)))

for i in reversed(sec2):
    print(i, end=', ')
print()

print(2*'\n')
# para hacer un loop sobre una secuencia de forma ordenada

sec3 = [7, 3, 8, 1, 4, 6, 9, 2, 5]

print(sec3)
for i in sorted(sec3):
    print(i, end= ', ')
print()
