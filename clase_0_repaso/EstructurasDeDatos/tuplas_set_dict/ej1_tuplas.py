# definir una tuple
a = 1,2,3,4,5,6,7
print(a)

b = ('a', 'e', 'i', 'o', 'u')
print(f'esta es otra tupla {b}')

c = (4.5, 7.2, 5.1,)
print(f'esta es una tupla de flotantes {c}')

d = 'uno', 'dos', 'tres', 'cuatro'
print(f'esta es una tupla de strings {d}')

# tupla de un elemento
e = 4,
print(f'una tupla de un solo elemento {e}')

f = tuple()
print(f)
print(id(f))

f = 45, 67, 82
print(f)
print(id(f))