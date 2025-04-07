frutas = ['naranja', 'manzana', 'pera', 'cambur', 'kiwi', 'manzana', 'cambur']

print(f'Hay {frutas.count("manzana")} manzanas')

print(f'El cambur está en el indice {frutas.index("cambur")}')

print(f'El siguiente cambur está en el indice {frutas.index("cambur", 4)}')

frutas.reverse()
print(frutas)

frutas.sort()
print(frutas)

last_fruta = frutas.pop()
print(last_fruta)
print(frutas)