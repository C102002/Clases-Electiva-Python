def numeros_fibonacci(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def cuadrado(nums):
    for num in nums:
        yield num**2

print(f"la suma es: {sum(cuadrado(numeros_fibonacci(10)))}")