class MiEstructura:
    def __init__(self, lista):
        self.lista = lista

    def __len__(self):
        return len(self.lista)


mi_estructura = MiEstructura([1, 2, 3, 4, 5])
# print(len(mi_estructura)) 

def pares_hasta(limite):
    x = 2
    while x <= limite:
        yield x
        x += 2

pares_hasta_20 = pares_hasta(20)

# for i in pares_hasta_20:
#     print(i)

