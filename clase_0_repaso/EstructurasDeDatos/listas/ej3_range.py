# creando una lista con range
lista = list(range(8))
print("\n", lista, end=" ")

print(10*"=")
# otro lista con range
listb = list(range(20, 35))
print("\n", listb, end=" ")

print(10*"=")
# mas listas con range
listc = list(range(30, 61, 3))
print("\n", listc, end=" ")

print("\n", 10*"=")
# trabajando con range()
var1 = range(20)
print(type(var1))
print(var1)

# como el range() es un iterable se puede recorrer con un for
for i in var1:
    print(i, end=" ")