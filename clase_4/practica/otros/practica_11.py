"""
Se tiene una lista de números enteros, la cual contiene valores repetidos,se desea crear una lista con los números no repetidos de la primera lista.Para probar use la siguente lista:
13, 10, 22, 18, 32, 39, 21, 5, 33, 15, 18, 2, 9, 31, 18, 7, 23, 27, 28, 9, 31,15, 7, 28, 18

Al final imprima ambas listas y la cantidad de elementos de cada una
Nota:
puede usar el operador “in”, pero no el concepto de “set

"""

list = [13, 10, 22, 18, 32, 39, 21, 5, 33, 15, 18, 2, 9, 31, 18, 7, 23, 27, 28, 9, 31,15, 7, 28, 18]
list_filtered=[]

for i in list:
    if i not in list_filtered:
        list_filtered.append(i)
        
print(f"data de la lista filtrada {list_filtered}")
