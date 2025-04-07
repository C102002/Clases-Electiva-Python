frutas = ['naranja', 'manzana', 'pera', 'cambur', 'kiwi', 'manzana', 'cambur']

# slicing:
trozo_frutas = frutas[0: 3]
print(trozo_frutas)
print(frutas)

# pertenencia
if 'manzana' in frutas:
    print('manzana está en frutas')

if 'lechoza' not in frutas:
    print('lechoza no esta en frutas')

# # concatenar listas:
flores = ['rosa', 'margarita', 'orquidea', 'girasol', 'azucena']
flores_frutas = flores + frutas
print(flores_frutas)

# # repetición
mas_flores = flores * 3
print(mas_flores)