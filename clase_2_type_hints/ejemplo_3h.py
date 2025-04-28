from typing import Annotated


def max_length(length: int):
    return lambda value: len(value) <= length


def validate_positive(x: int) -> bool:
    return x > 0


# Usando Annotated para acoplar la metadata a los type hints
Name = Annotated[str, max_length(10)]
Age = Annotated[int, validate_positive]


def register_user(name: Name, age: Age) -> None:
    print(f"Usuario registrado {name} edad {age}")


register_user("Pedro Perez", Age(18))