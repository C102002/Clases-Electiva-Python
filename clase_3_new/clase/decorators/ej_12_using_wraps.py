from functools import wraps

def my_decorator(function):
    """Este será el Docstring para el decorador"""
    @wraps(function)
    def wrapper(*args, **kwards):
        print("Llamando a la función decorada")
        return function(*args, **kwards)
    return wrapper


@my_decorator
def example():
    """Docstring de ejemplo"""
    print("Llamada a la función example")


print(example())
print()
print(example.__name__)
print()
print(example.__doc__)