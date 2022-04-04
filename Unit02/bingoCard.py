# Realizar un programa que genere 15 números aleatorios enteros en el rango del 1 al 100, que representaria la tarjeta de bingo de una persona. Una vez generados los números aleatorios solicitar al usuario que ingrese 3 números enteros y a partir de alli mostrar los siguientes mensajes:

# Si el usuario no marcó ninguno de los números indicarlo diciendo "El jugador tiene mala suerte, no marcó ninguna casilla"
# Caso contrario mostrar "El jugador marcó algún numero de la tarjeta".

import random


r1 = random.randrange(1, 100)
r2 = random.randrange(1, 100)
r3 = random.randrange(1, 100)
r4 = random.randrange(1, 100)
r5 = random.randrange(1, 100)
r6 = random.randrange(1, 100)
r7 = random.randrange(1, 100)
r8 = random.randrange(1, 100)
r9 = random.randrange(1, 100)
r10 = random.randrange(1, 100)
r11 = random.randrange(1, 100)
r12 = random.randrange(1, 100)
r13 = random.randrange(1, 100)
r13 = random.randrange(1, 100)
r14 = random.randrange(1, 100)
r15 = random.randrange(1, 100)
print(r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15)


n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))
n3 = int(input('Enter the third number: '))


if n1 == r1 or n1 == r2 or n1 == r3 or n1 == r4 or n1 == r5 or n1 == r6 or n1 == r7 or n1 == r8 or n1 == r9 or n1 == r10 or n1 == r11 or n1 == r12 or n1 == r13 or n1 == r14 or n1 == r15:
    print('El jugador marcó algún numero de la tarjeta')
elif n2 == r1 or n2 == r2 or n2 == r3 or n2 == r4 or n2 == r5 or n2 == r6 or n2 == r7 or n2 == r8 or n2 == r9 or n2 == r10 or n2 == r11 or n2 == r12 or n2 == r13 or n2 == r14 or n2 == r15:
    print('El jugador marcó algún numero de la tarjeta')
elif n3 == r1 or n3 == r2 or n3 == r3 or n3 == r4 or n3 == r5 or n3 == r6 or n3 == r7 or n3 == r8 or n3 == r9 or n3 == r10 or n3 == r11 or n3 == r12 or n3 == r13 or n3 == r14 or n3 == r15:
    print('El jugador marcó algún numero de la tarjeta')
else:
    print('El jugador tiene mala suerte, no marcó ninguna casilla')
