# definiendo un set
seta = {1,3,5,7,9}

print(f'esto es un set: {seta}')

# recorrer un set:
for i in seta:
    print(i, end=' ')
print()

# agregar elemento al set
seta.add(14)
print(f'el set A despues de agregar un elemento:  {seta}')

# obtener un elemento de un set
elem = seta.pop()
print(f'elemento obtenido: {elem}')

# guardar un string en un set
string = 'ab cde fab c'
setc = set(string)
print(setc)

setd = set(range(10))
print(setd)


