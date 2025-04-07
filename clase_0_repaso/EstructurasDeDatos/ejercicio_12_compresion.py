# comprension simple:
cubos = [i**3 for i in range(1, 8)]

print(cubos)


# compresion con condición
cubos = [i**3 for i in range(1, 8) if i %2 == 0]
print(cubos)


#compresion anidada:
matrix = [[j for j in range(5)] for i in range(5)]
print(matrix)

# aplanando una matriz
listb = [[1, 2, 3], [4, 5], [6, 7, 8, 9] ]

print(listb)

listb_plana = [val for sub_list in listb for val in sub_list] 
print(listb_plana)

