a_dict = {'color': 'azul', 'fruta': 'manzana', 'mascota': 'perro'}

# para ver las claves
print('por claves:')
for key in a_dict:
    print(key)
print()

# para ver las claves y sus valores
print('por claves y valor:')
for key in a_dict:
    print(key, '->', a_dict[key])
print()

# usando items()
print('usando items()')
for item in a_dict.items():
    print(item)
print()

print('usando items(), otra forma')
for key, value in a_dict.items():
    print(key, '->', value)
print()

# para más ejemplos ver https://realpython.com/iterate-through-dictionary-python/
