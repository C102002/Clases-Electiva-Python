lista = ["Juan", "Maria", "José", "Rosa"]
listb = ["Roberto", "Susana", "Diego", "Xiomara"]
lista.extend(listb)

print(f"lista: {lista}")

print(f"el indice de Susana: {lista.index('Susana')}")

print(f"el indice que no esta en lista: {lista.index('Javier')}")

