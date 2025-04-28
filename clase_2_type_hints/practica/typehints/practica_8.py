def numeros_fibonacci(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def cuadrado(nums):
    for num in nums:
        yield num**2

for value in numeros_fibonacci(10):
    
    print(f"el numero es:{value}")
    
    for square in cuadrado([value]):  # Pasar el número como lista
        print(f"El cuadrado del numero es: {square}")

print(f"la suma es: {sum(cuadrado(numeros_fibonacci(10)))}")