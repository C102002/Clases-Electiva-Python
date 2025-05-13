"""
Cree una función decoradora que permita indicar cuál es el tiempode ejecución que tarda en procesarse la función a la cual decora,Ayudas:
a. La función decoradora coloque el nombre calcula_tiempo
b. para usarla va a necesitar el módulo time de Python (importe lo usando import time),
el cual tiene una función llamada time()
quedevuelve el momento actual.
c. Para probar su decorador use el siguiente código:
"""

from functools import wraps
from time import time

def calcula_tiempo(function):
    """Este será el Docstring para el decorador"""
    @wraps(function)
    def wrapper(*args, **kwards):
        start_time=time.time()
        value=function(*args, **kwards)
        end_time=time.time()
        print(f"El tiempo total en ejecutar fue de {end_time-start_time} segundos")
        return value
    
    return wrapper

import math
import time
@calcula_tiempo
def factorial (num):
    time.sleep(2)
    print(math.factorial(num))
    
# d.pruebe llamado a la función factorial con un valor de num = 10 (factorial(10))
num=factorial(10)
# f. Al ejecutar el código del punto d, debe aparecer, junto con el valor del factorial de 10, un mensaje que indique lo siguiente: "El tiempo total en ejecutar fue de ___ segundos", donde el espacio en blanco se sustituirá por el valor calculado.
