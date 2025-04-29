# Cree una función decoradora que permita indicar cuál es el tiempo de ejecución que tarda en procesarse la función a la cual decora.

# Ayudas:
# a. La función decoradora debe llamarse calcula_tiempo. 
# b. Para usarla, necesitarás importar el módulo time de Python (import time), que contiene la función time() para obtener el momento actual. 
# c. Para probar tu decorador, usa el siguiente código:

import math
import time

def calcula_tiempo(function):
    def wrapper(num:int):
        time_start=time.time()
        r=function(num)
        time_end=time.time()
        print(f"Eltiempo total en ejecutar fue de {time_end-time_start} segundos ")
        return r
    return wrapper

@calcula_tiempo
def factorial(num):
    time.sleep(2)
    print(math.factorial(num))

factorial(10)