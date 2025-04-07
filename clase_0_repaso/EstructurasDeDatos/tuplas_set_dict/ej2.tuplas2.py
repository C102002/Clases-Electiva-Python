a = 1,2,3,4,5,6,
b = ('a', 'b', 'c', 'd')

c = a + b
print(f'usando el operador + {c}')

print(f' el maximo en a es {max(a)}')

# para averiguar si tienen un elemento o no
frase = "en mi casa tengo una mesa verde"
# averiguar un elemento en particular:
if 'b' in b:
    print('lo contiene')
else:
    print('no lo contiene')

print('-----------')

for elem in frase:
    if elem in b:
        print(f'el elemento {elem} es una letra en la tuple b')
    else:
        print(f'el elemento {elem} no es una letra en la tuple b')
        
print(30*'-')
        
lista=[]        
for item in c:
    lista.append(item)

print(c)    
print(lista)

d = (a, b, lista)
print('esta es la tupla d: ', d)

print(len(d))