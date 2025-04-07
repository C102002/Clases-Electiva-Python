# ejemplo de una lista
frutas = ['naranja', 'manzana', 'pera', 'cambur', 'kiwi', 'manzana', 'cambur']
print(frutas)

# reversando una lista
frutas.reverse()
print(frutas)

# agregando elementos a una lista
frutas.append('fresa')
print(frutas)

# ordenando los elementos de una lista
frutas.sort()
print(frutas)

# obteniendo el último elemento de la lista
fruta = frutas.pop()
print(fruta)

frutas2 = ['naranja', 'manzana', 'pera', 'manzana', 'kiwi', 'manzana', 'cambur']

total_manzana = frutas.count('manzana') + frutas2.count('manzana')
print('total de manzanas:',total_manzana)