# ¿Cómo se implementa la función dunder
# __getitem__
# para acceder aelementos de una lista personalizada, llámela MiLista? (Muestre elcódigo)
# Para probar use lo siguiente:


class MiLista:
    def __init__(self, items:list[int])->None:
        self.items=items
    
    def __getitem__(self, value: int) -> int:
        return self.items.__getitem__(value)
    
mi_lista = MiLista([10, 20, 30, 40, 50])
print(mi_lista[2]) # Debería imprimir 30