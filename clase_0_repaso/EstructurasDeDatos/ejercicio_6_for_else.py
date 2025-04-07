for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'es igual a', x, '*', n//x)
            break
    else:
        print(n, 'es un número primo')    