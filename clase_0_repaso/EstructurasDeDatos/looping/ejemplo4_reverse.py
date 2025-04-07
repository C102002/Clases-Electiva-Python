# invirtiendo una lista
print('invirtiendo una lista')
sistemas = ['Windows', 'macOS', 'Linux']
print('lista original', sistemas)
sistemas.reverse()
print('lista invertida', sistemas)
print()

# invirtiendo una lista usando el operador slice
print('invirtiendo una lista usando el operador slice')
sistemas = ['Windows', 'macOS', 'Linux']
print('lista original', sistemas)
sistemas_invertido = sistemas[::-1]
print('lista invertida', sistemas_invertido)
print()

# Accediendo elementos en orden inverso
print('Accediendo elementos en orden inverso')
sistemas = ['Windows', 'macOS', 'Linux']
for o in reversed(sistemas):
    print(o)
print(sistemas)
