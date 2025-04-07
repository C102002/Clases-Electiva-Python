lista = ["Juan", "Maria", "José", "Rosa"]

print(f"lista antes del pop: {lista}")

nombre = lista.pop()

print(f"lista después del pop: {lista}")
print(f"el valor de nombre es: {nombre}")

print("\nusando un índice\n")

nombre2 = lista.pop(1)
print(f"el valor de nombre es: {nombre2}")