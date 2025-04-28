from typing import Callable


def perform_action(action: Callable[[int, int], str], x: int, y: int) -> None:
    result = action(x, y)
    print(f"Resultado de la acción: {result}")


def sum_two(a: int, b: int) -> str:
    return f"La suma es: {a + b}"


perform_action(sum_two, 5, 3)
# Action Result: The sum is: 8