#crear el objeto generador
generador_cuadrados = (i * i for i in range(5))

# iterar sobre el generador e imprimir los valores
for i in generador_cuadrados:
    print(i)
