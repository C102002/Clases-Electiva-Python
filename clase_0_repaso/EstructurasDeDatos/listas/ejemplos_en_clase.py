frutas = ['naranja', 'manzana', 'pera', 'cambur', 'kiwi', 'manzana', 'cambur']

# frutas.append('piña')
# print(frutas)

# frutas.insert(3, 'lechoza')

# print(frutas)

# for item in frutas:
#     print(item, end=', ')
# print()

# una_fruta = frutas.pop()
# print(una_fruta, ' - ', frutas)

# print(frutas)
# frutas.reverse()
# print(frutas)
# frutas.sort()
# print(frutas)
# frutas.sort(reverse=True)
# print(frutas)

frutas = ['naranja', 'manzana', 'pera', 'cambur', 'kiwi', 'manzana', 'cambur']
flores = ['rosa', 'margarita', 'orquidea', 'girasol', 'azucena']

idx = 0
lista_nueva = list()
while idx < len(flores):
    lista_nueva.append(flores[idx] + frutas[idx])
    idx += 1
    
print(lista_nueva)

# contar frutas repetidas:
