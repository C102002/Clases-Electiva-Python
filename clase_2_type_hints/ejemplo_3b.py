from typing import TypeVar, Tuple

T = TypeVar('T')
Y = TypeVar('Y')

def swap(x: T, y: Y) -> Tuple[Y, T]:
    return y, x

result: Tuple[int, int] = swap(1, 2)
result2: Tuple[str, int] = swap(6, 9)