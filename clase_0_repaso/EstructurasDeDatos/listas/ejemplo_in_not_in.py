lista = list(range(-10, 10, 2))

print(7 in lista)

if 7 in lista:
    print("está")
else:
    print("no está")

x = "esta" if 7 in lista else "no está"
print(x) 