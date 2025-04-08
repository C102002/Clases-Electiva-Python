# Se tiene una lista de números enteros, la cual contiene valores repetidos,se desea crear una lista con los números no repetidos de la primera lista.Para probar use la siguente lista:
# 13, 10, 22, 18, 32, 39, 21, 5, 33, 15, 18, 2, 9, 31, 18, 7, 23, 27, 28, 9, 31,15, 7, 28, 18
# Al final imprima ambas listas y la cantidad de elementos de cada una
# Nota:
# puede usar el operador “in”, pero no el concepto de “set”


# Defina un diccionario llamado informacion_persona, que contengainformación básica de una persona: nombre, edad, ciudad y correoelectrónico.
# En el mismo código cree una variable que acceda a la información deedad y la imprima en el terminal de la computadora
def order_list(list):
    list_no_repetidos = []
    for i in list:
        if i not in list_no_repetidos:
            list_no_repetidos.append(i)
    return list_no_repetidos

if __name__ == "__main__":
    
    list = [13, 10, 22, 18, 32, 39, 21, 5, 33, 15, 18, 2, 9, 31, 18, 7, 23, 27, 28, 9, 31,15, 7, 28, 18]
    print(list)
    list_filtered= order_list(list)
    print(list_filtered)