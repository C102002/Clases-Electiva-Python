# sort, modifica la lista
# sorted(), no modifica la lista

# ejemplo 1. sorted()
print('usando sorted()')
numeros = [6, 9, 3, 1, 7, 4]
print('ordenado con sorted', sorted(numeros))
print('list orginal', numeros)
print()

# ejemplo 2, manteniendo el ordenamiento
print('manteniendo el ordenamiento')
numeros = [6, 9, 3, 1, 7, 4]
numeros_ordenados = sorted(numeros)
print('original', numeros)
print('ordenada', numeros_ordenados)

# ejemplo 3, ordenando strings
print('ordenando strings')
string_numerico = '34521'
string_literal = 'Esto es un string'
string_numerico_ordenado = sorted(string_numerico)
string_literal_ordenado = sorted(string_literal)
print(string_numerico_ordenado)
print(string_literal_ordenado)
print()

# ejemplo 4, usando el argumento reverse
print('usando el argumento reverse')
names = ['Luis', 'Susana', 'Antonio', 'Marcos']
print('original', names)
print('ordenados:',sorted(names))
print('ordenados inverso',sorted(names, reverse=True))
print()

# ejemplo 5, usando el argumento key
print('usando el argumento key (longitud)')
names = ['Humberto', 'Susana', 'Antonio', 'Marcos', 'Luis' ]
print('original', names)
print('ordenados por len():',sorted(names, key=len))
print()
