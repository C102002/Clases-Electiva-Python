# La palabra with se usa en Python para gestionar un contexto, lo que permite abrir un archivo sin necesidad de cerrarlo manualmente, ya que el gestor de contexto lo maneja automáticamente.

# Para crear un gestor de contexto, se implementan los métodos __enter__() y __exit__() para definir la entrada y salida, respectivamente, del contexto.

# Crea una clase llamada Timer, que aplicada a una iteración cualquiera mida el tiempo de ejecución de la iteración.
import time

class Timer:
    def __init__(self):
        self.start=0
        self.end=0
        pass
    def __enter__(self):
        self.start=time.time()
        pass
    def __exit__(self, exc_type, exc_value, traceback):
        self.end=time.time()
        print (f"el tiempo total en s {(self.end-self.start)}")
        pass

with Timer():
# Bloque de código para medir el 
    for _ in range(1000000):
        pass