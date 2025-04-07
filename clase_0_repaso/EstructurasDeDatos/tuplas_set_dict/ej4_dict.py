# creado un diccionario:

dicta= {'a':1, 'b':2, 'c':3, 'd':4}
print(dicta)

print(list(dicta))

# obtener un valor a partir de una clave:
valor = dicta.get('b')
print(valor)

# los elementos de un diccionario (clave: valor)
elementos = list(dicta.items())
print(elementos)

# claves:
claves = list(dicta.keys())
print(claves)

# valores:
valores = list(dicta.values())
print(valores)

dick = {2: 'a', 3: 6}
print(dick)

# recorriendo un diccionario
for k,v in dicta.items():
    print(f'para la clave {k}, se tiene el valor {v}')

dictb = {'camisa': 100, 'pantalon': 120, 'short':30, 'zapato deportivo': 100}
print(dictb)
print(id(dictb))
pp = dictb.get('pantalon')
print(pp)

dictb.update({'pantalon':110})
print(dictb)
print(id(dictb))

var1 = dictb.get('falda', 150)

print(var1)
print(dictb)

print(len(dictb))
