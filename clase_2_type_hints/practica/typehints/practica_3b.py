from typing import Generic, Optional, TypeVar

# Practica haciendo el Result

T = TypeVar('T')

class Result(Generic[T]):
    def __init__(self, value: Optional[T], error: Optional[Exception]) -> None:
        self.value = value
        self.error = error

    def __repr__(self) -> str:
        return f"Result(value={self.value}, error={self.error})"
    
    @staticmethod
    def success(value: T) -> "Result[T]":
        return Result(value=value, error=None)
    
    @staticmethod
    def fail(error: Exception) -> "Result[T]":
        return Result(value=None, error=error)
    
# Codigo de ejemplo
r1:Result[int]=Result.success(4)
print(f"result1: {r1}")

r2:Result[Exception]=Result.fail(Exception("fallo"))
print(f"result2: {r2}")
