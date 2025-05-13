"""¿Cómo se implementa la función dunder __len__ para obtener la longitud de una
estructura de datos personalizada, llámela MiEstructura? (Muestre el código)
Para probar use lo siguiente:"""

class MiEstructura:
    def __init__(self,list:list):
        self.list=list
        pass
    def __len__(self):
        return len(self.list)

mi_estructura = MiEstructura([1, 2, 3, 4, 5])
print(len(mi_estructura)) # Debería imprimir 5