# ¿Cómo se implementa la función dunder
# __getitem__
# para acceder aelementos de una lista personalizada, llámela MiLista? (Muestre elcódigo)

class MiLista:
    def __init__(self, lista:list):
        self.lista = lista
    def __getitem__(self, index):
        if index not in self.lista:
            raise ValueError("Error: el valor no está en la lista")
        return self.lista.index(index)  # Devuelve la posición del elemento

        

# Para probar use lo siguiente:
mi_lista = MiLista([10, 20, 30, 40, 50])
print(mi_lista[20]) # Debería imprimir 1