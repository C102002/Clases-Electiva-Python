frutas = ['naranja', 'manzana', 'pera', 'cambur', 'kiwi', 'manzana', 'cambur']
print(frutas)

# #cambiar un elemento de la lista
# idx = frutas.index('pera')
# fruta = frutas[idx]
# print(fruta)

# fruta += ' verde'
# frutas[idx] = fruta
# print(frutas)

# # intercambiar posiciones:
# i = 0
# while i < len(frutas) - 1:
#     frutas[i], frutas[i+1] = frutas[i+1], frutas[i]
#     print(frutas)
#     i +=1

# print(frutas)

# otro ejemplo 
# listb = list(range(10, 20, 2))
# print(listb)

# listc = list(range(50, 30, -3))
# print(listc)

# listb.append(listc)
# print(listb)

#mini buscador
# resp = 's'
# while resp == 's':
#     fruta = ['manzana', 'naranja','patilla','tomate'] 
#     varEntrada = input('Ingrese la fruta buscada: ') 
#     varComp = 0 
#     while varComp == 0: 
#         if varEntrada in fruta: 
#             print('En la lista fruta hay',varEntrada) 
#             varComp = 1 
#         else: 
#             print('el elemento no se encuentra en la lista') 
#             varComp = 1
    
#     resp = input('¿Desea continuar [s/n]?')