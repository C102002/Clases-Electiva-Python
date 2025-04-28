from typing import Callable, TypeVar

T = TypeVar('T')
Y = TypeVar('Y')


def perform_action(action: Callable[[T], str], var: T) -> None:
    result = action(var)
    print(f"Resultado de la accion: {result}")

# Una forma de hacerlo generico
    
def perform_any_action(action: Callable[[T], Y], var: T) -> None:
    result = action(var)
    print(f"Resultado de la accion: {result}")
    
# ? Posible funcion para meter n elementos a una lista

def push_many_elements(action: Callable[..., list[T]], *args: T) -> None:
    result = action(*args)
    print(f"Resultado de la acción: {result}")


def print_number(a: int) -> str:
    return f"El valor es es: {a}"


perform_action(print_number, 5)
# Imrpime Resultado de la accion: El valor es es: 5

perform_any_action(print_number,5)