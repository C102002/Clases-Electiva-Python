mantenerse = 's'
while mantenerse == 's':
    fah = int(input('Ingrese una temperatura en °Fahrenheit: '))
    cel = (fah - 32) * 5/9
    print(f'{fah}°F son {round(cel,1)}°C')

    mantenerse = input('Desea continuar [s/n]? ')

print('Finalizó el programa')