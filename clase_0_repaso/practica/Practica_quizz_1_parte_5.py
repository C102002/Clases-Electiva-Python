# La palabra with se usa en Python para gestionar un contexto, es asícomo se puede abrir un archivo usando with y no hay necesidad decerrarlo, ya que el gestor se encarga de ello. Para crear un gestor decontexto se implemetan los métodos __enter__() y __exit__() paradefinir la entrada y salida respectivamente del contexto. Cree un clasellamada Timer, que aplicada a una iteración cualquiera mida el tiempode ejecución de la iteración.

# Ayuda: debe importar el módulo time y usar el método time() paraobtener el tiempo actual de la máquina. Además en la implemnetacióndel metodo __exit__() debe tener un mensaje que indique el tiempotranscurrido en segundos. Para probar la funcionalidad de su clasehágalo con el siguiente código:
# with Timer():
# Bloque de código para medir el tiempo de ejecución
# for _ in range(1000000):
# pass
# Copia tu código con la respuesta en el lugar indicado.

import time
class Timer:
    def __enter__(self):
        self.inicio_time=time.time()
    def __exit__(self,exc_type,exc_val,exc_tb):
        fin_time=time.time()
        transcurrido_time=fin_time-self.inicio_time