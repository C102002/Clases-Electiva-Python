# En la página oficial de
# Python (https://www.python.org/)
# , en elcarrusel de la página principal, existe un código para generar la seriede Fibonacci de forma iterativa con un ciclo while. Modifique lafuncionalidad para que sea realizada con una función generadora,luego con un ciclo iterativo usando la función realizada entregue losprimeros 15 números de la serie. Copia tu código con la respuesta enel lugar indicado.
# 
def fibonacci(secuencia, n):
    """Generador de la serie de Fibonacci""" 
    # yield a da la secuencia de valores de la serie de Fibonacci
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    # Generar los primeros 15 números de la serie de Fibonacci
    n = 15
    secuencia = fibonacci(secuencia=[], n=n)
    
    # Imprimir los números generados
    for num in secuencia:
        print(num, end=' ')
    print()


# #funcion generadora:
# def fibonacci():
# a, b = 0, 1
# while True:
# yield a
# a, b = b, a + b
# fibonacciR = (x for x in fibonacci())
# for i, number in enumerate(fibonacciR, 1):
# print(number)
# if i == 15:
# break