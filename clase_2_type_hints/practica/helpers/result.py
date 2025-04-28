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
    
    def isSucsess(self)->bool:
        if self.value == None:
            return True
        else:
            return False