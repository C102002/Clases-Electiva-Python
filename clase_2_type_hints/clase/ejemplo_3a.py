from typing import TypeVar, List

T = TypeVar('T')

def get_first(l: List[T]) -> T:
    return l[0]

numbers: List[int] = [1, 2, 3]

result: int = get_first(numbers) # usado correctamente
result2: str = get_first(numbers) # no usado correctamente (lanza error)