# Cree una función generadora llamada baraja() que simule la entrega de cartas de un mazo.
# Usa las siguientes listas para definir el mazo de cartas:

valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
palos = ['corazones', 'diamantes', 'tréboles', 'picas']

# Para probar

def baraja()->tuple[str,str]:
    for i in palos:
        for j in valores:
            yield (j,i)

i: int = 0
print("todos las cartas")
for carta in baraja():
    print(carta)
    
print(25*"-")

for carta in baraja():
    print(carta)
    i += 1
    if i > 5:
        break
# La función debe entregar una tupla (valor, palo), por ejemplo: ("3", "diamantes").
