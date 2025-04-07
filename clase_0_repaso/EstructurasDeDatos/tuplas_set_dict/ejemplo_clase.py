lista = list(range(5, 50, 2))
print(lista)

listb = [x**3 for x in range(1,11)]
print(listb)

listc = ["casa", "caballo", "perro", "avion", "tabla"]

listd = [item for item in listc if "c" in item]
print(listd)

var1 = """el que salga de ultimo que apague la luz y
 los murcielagos vuelan entre los arboles de cerezo"""

tupla = "a", "e", "i", "o", "u"
liste = [x for x in var1 if x in tupla]
print(liste)

listee = [x for x in var1 if x=="a" or x=="e" or x=="i" or x=="o" or x=="u"]
print(listee)
