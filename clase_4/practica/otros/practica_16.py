"""
1. Crea un decorador llamado resultado_en_mayusculas.
2. Este decorador debe hacer lo siguiente:

* Ejecutar la función decorada original con todos sus argumentos.
* Tomar el valor que retorna la función original.
* Si el valor retornado es una cadena de texto (str), convertir esa cadena a mayúsculas.
* Si el valor retornado no es una cadena de texto, devolverlo tal cual, sin modificarlo.
* Devolver el resultado (convertido a mayúsculas o el original).

3. Define una función simple (por ejemplo, obtener_saludo) que acepte un argumento (ej. un nombre) y devuelva una cadena de texto (ej. "hola, [nombre]").
4. Define otra función simple (por ejemplo, sumar_dos_numeros) que devuelva un tipo diferente a str (por ejemplo, un int).
5. Aplica el decorador @resultado_en_mayusculas a ambas funciones.
6. Llama a las funciones decoradas y verifica que:
* El resultado de obtener_saludo se devuelva en mayúsculas.
* El resultado de sumar_dos_numeros se devuelva sin cambios.
7. Asegúrate de usar type hints en la definición del decorador y en las funciones decoradas.

Ejemplo de implementación parcial y uso:"""

from typing import Callable, Any, TypeVar
from functools import wraps


# Definición del decorador (a completar por el estudiante)
F = TypeVar('F', bound=Callable[..., Any])

def resultado_en_mayusculas(func: F) -> F:
    @wraps(func)
    def wrapper(*args, **kwards):
        result=func(*args,**kwards)
        if type(result)==str:
            return result.upper()
        return result

    return wrapper

# --- Funciones de ejemplo ---

@resultado_en_mayusculas
def obtener_saludo(nombre: str) -> str:
     '''Genera un saludo en minúsculas.'''
     return f"hola, {nombre}!"

@resultado_en_mayusculas
def sumar_dos_numeros(a: int, b: int) -> int:
     '''Suma dos enteros.'''
     return a + b

# --- Llamadas ---
saludo_modificado = obtener_saludo("mundo")
print(f"Saludo modificado: {saludo_modificado}")

suma_original = sumar_dos_numeros(5, 3)
print(f"Suma sin modificar: {suma_original}")

# Salida esperada:
# Saludo modificado: HOLA, MUNDO!
# Suma sin modificar: 8