lista = list(range(5))
print(lista)

listb = list(range(10, 30, 3))
print(listb)

cubos = [i**3 for i in range(10)]
print(cubos)

cubos2 = [i**3 for i in range(10) if i%2 == 0]
print(cubos2)

# a partir de un for:
listx = []
for i in range(0, 10, 2):
    x = i**3 + i**2 + i/2
    listx.append(x)
print(listx)

listy = [i**3 + i**2 + i/2 for i in range(0, 10, 2)]
print(listy)

listz = []
for x in range(20, 25):
    listz.append(x + 0.5*x)
    for y in range(10, 13):
        listz.append(y + 2)
print(listz)

listw = [(x + 0.5*x for x in range(20, 25)) + (y + 2 for y in range(10, 13))]
print(listw)