# ¿Cómo se implementa la función dunder __len__ para obtener la longitud de una
# estructura de datos personalizada, llámela MiEstructura? (Muestre el código)

class PersonalStructure:
    def __init__(self,datos:list[int]):
        self.datos = datos
    def __len__(self)->int:
        return len(self.datos)
    
    
personal=PersonalStructure(datos=[1,2,3,4,5,6])
print(f"el valor de len {personal.__len__()}")