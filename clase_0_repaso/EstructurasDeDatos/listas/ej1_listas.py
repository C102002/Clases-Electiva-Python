# ejemplo de una lista
frutas = ['naranja', 'manzana', 'pera', 'cambur', 'kiwi', 'manzana', 'cambur']


# visualización de una lista 
print(frutas)


#ver el tipo
print(type(frutas))


# contar elemento de una lista
print('\n',frutas.count('manzana'))
print('\n',frutas.count('mandarina'))


# localizar el indice de un elemento
print('\n',frutas.index('cambur'))
# localizar el indice de un elemento a partir de otro indice
print('\n',frutas.index('cambur', 4))


print('\n',len(frutas))

print('\n',frutas.index('kiwi', -5))
