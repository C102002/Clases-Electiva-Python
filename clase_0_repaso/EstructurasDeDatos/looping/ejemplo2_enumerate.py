# enumerate más básico
print('básico: ')
browsers = ['Chrome','Firefox','Opera','Vivaldi']
x = list(enumerate(browsers))
print(x)
print()


# usado como un iterator:
print('como iterator')
eObj = enumerate(browsers)

x = next(eObj)
print(x)
x = next(eObj)
print(x)
print()

# enumerando una lista
print('enumerate en una lista')
frutas = [ "Naranja","Cambur","Piña" ]
for i,j in enumerate(frutas):
    print(i,j)
print()

# enumerando tuples
print('enumerate en tuples')
numeros = [(1, 'uno'), (2, 'dos'), (3, 'tres') ]
for i,j in enumerate(numeros):
    print(i,j)
print()

# enumerate con desempaque de tuple
print('con desempaque de tuple')
precios = [(15,"Manzana"), (12,"Cambur"), (19,"Fresa")]
for i,(price,name) in enumerate(precios):
    print(f"index {i}, precio {price} y nombre {name}")

# enumerando un string
print('enumerate en un string')
fruta = "Naranja"
for i,j in enumerate(fruta):
    print(i,j)
print()    

# enumerando con indice de arranque diferente
print('enumerate con indice de arranque diferente')
fruta = "Naranja"
for i,j in enumerate(fruta, start=2):
    print(i,j)
print() 

# enumerando diccionarios
print('enumerate en un diccionario')
d = {'a':1, 'b':2, 'c': 3}
for i,j in enumerate(d.items()):
    print(i,j)
print()
