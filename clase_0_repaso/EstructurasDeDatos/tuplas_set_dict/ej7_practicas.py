lista = [2,4,6,8,9,23,43,24,56,12,34]
listb = [5,4,2,4,6,67,3,2,5,54,23]

print(lista, end=' ')
print()
for idx, val in enumerate(lista):
    print(idx, val)
print()

print(listb, end=' ')
print()
listc = list()

d = list(zip(lista, listb))
print('d:', d)

for dup in zip(lista, listb):
    #el zip retorna un tuple
    print(dup)
    # descomposición de tuple
    a, b = dup
    listc.append(a + b)

print(listc)

print(30*'-')

diccionario = dict() 
str = 'Excepteur officia eiusmod laborum do incididunt elit. Consectetur ea duis aute commodo velit Lorem cupidatat fugiat aute reprehenderit reprehenderit commodo. Dolore id velit voluptate ullamco nostrud. Fugiat elit nisi irure sunt nostrud sunt proident eiusmod. Cillum est ea amet adipisicing dolor enim labore reprehenderit.' 
for letra in str: 
    diccionario[letra] = diccionario.get(letra,0)+1 
    
print(diccionario) 