lista = ['casa', 'perro', 'silla', 'cocina']
print(lista)
print('lista está en la posición:', id(lista))

lista[2] = 'pelota'
print(lista)
print('lista está en la posición:', id(lista))

lista.append('lapiz')
print(lista)
print('lista está en la posición:', id(lista))

print(f"la posición de perro es {lista.index('perro')}")