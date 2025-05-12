# Crea una función generadora llamada potencias(numero, exponente),que devuelva las potencias sucesivas de un número dado,comenzando por 1 y elevando hasta un exponente especificado.

def potencias(numero:int,exponente:int):
    n=1
    while(n<=exponente):
        yield numero**n
        n+=1

# Para probar use lo siguiente:
potencias_2 = potencias(2,5)
# Generador de potencias de 2 hasta la 5ª
for potencia in potencias_2: 
    print(potencia) # Salida: 2 4 8 16 32