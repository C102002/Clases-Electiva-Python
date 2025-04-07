# ejemplo usando extend
lista = ["Juan", "Maria", "José", "Rosa"]

listb = ["Roberto", "Susana", "Diego", "Xiomara"]

lista.extend(listb)

print(lista)
for item in lista:
    print(item, end=", ")