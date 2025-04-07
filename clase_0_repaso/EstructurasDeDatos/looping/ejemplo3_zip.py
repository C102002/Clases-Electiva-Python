numeros = [1, 2, 3]
letras = ['a', 'b', 'c']
zipped = zip(numeros, letras)

# básico
print(type(zipped))
print(list(zipped))
print()


# con un solo argumento
print('con un solo argumento')
zipped = zip(letras)
print(list(zipped))
print()

# con más de dos argumentos
flotantes = [1.2, 5.67, 3.6]
print('con más de dos argumentos')
zipped = zip(numeros, letras, flotantes)
print(list(zipped))
print()

# con argumentos de diferente longitud
print('con argumentos de diferente longitud')
zipped = zip(range(5), range(50, 100))
print(list(zipped))
print()

# transversando listas en paralelo
print('transversando listas en paralelo')
for l, n in zip(letras, numeros):
    print(f'letra: {l}')
    print(f'numero {n}')
print()

print('transversando listas en paralelo, mas de dos argumentos')
operadores = ['*', '/', '+']
for l, n, o in zip(letras, numeros, operadores):
    print(f'letra: {l}')
    print(f'numero {n}')
    print(f'operador {o}')
print()

# transversando diccionarios en paralelo
print('transversando diccionarios en paralelo')
dic_1 = {'nombre': 'Juan', 'apellido': 'Perez', 'cargo': 'programador python' }
dic_2 = {'nombre': 'María', 'apellido': 'Romero', 'cargo': 'diseñador web' }
for (k1, v1), (k2, v2) in zip(dic_1.items(), dic_2.items()):
    print(k1, '->', v1)
    print(k2, '->', v2)
print()

# descomponiendo un secuencia:
print('descomponiendo un secuencia')
pares = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
numbers, letters = zip(*pares)
print(numbers)
print(letters)
print()

# Ordenando en paralelo
print('Ordenando en paralelo')
letras = ['b', 'a', 'd', 'c']
numeros = [2, 4, 3, 1]
data1 = list(zip(letras, numeros))
print(f"data1: {data1}")
data1.sort()  # ordenado por letras
print(f"data1 ordenado: {data1}")
data2 = list(zip(numeros, letras))
print(f"data2: {data2}")
data2.sort()  # ordenado por números
print(f"data2 ordenado: {data2}")
print()

#calculos en pares
print('calculos en pares')
total_ventas = [52000.00, 51000.00, 48000.00]
costo_prod = [46800.00, 45900.00, 43200.00]
for ventas, costos in zip(total_ventas, costo_prod):
    ganancia = ventas - costos
    print(f'Total ganancia: {ganancia}')
print()

# construyendo un diccionario
print('construyendo un diccionario')
campos = ['nombre', 'apellido', 'edad', 'cargo']
valores = ['Juan', 'Perez', '34', 'Desarrollador Python']
un_dict = dict(zip(campos, valores))
print(un_dict)