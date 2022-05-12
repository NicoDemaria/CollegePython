# 2. Ejercicio con secuencia de números aleatorios
# Generar una secuencia de n números aleatorios. El valor de n se ingresa por teclado, validar que sea mayor a 0.
#
# Determinar:
#
# a) Cuántos números terminan en 5.
#
# b) El porcentaje de números pares en la secuencia.
#
# c) Cual es el menor número múltiplo de 3 de la secuencia.
#
# d) La cantidad de veces que aparece el primer número de la secuencia.




numeros5 = 0
pares = 0
men = 1

import random
n = int(input('Ingrese la cantidad de numeros a generar: '))
if n > 0:
    for i in range(n):
        num = random.randint(1,1000)
        print(num)
        # # a) Cuántos números terminan en 5.
        if num % 10 == 5:
            numeros5 += 1
        # b) El porcentaje de números pares en la secuencia.
        if num % 2 == 0:
            pares += 1
            porcentaje = (pares*100) / n
        # c) Cual es el menor número múltiplo de 3 de la secuencia.
        if num % 3 == 0:
            if i == 1:
                men = num
            else:
                if num < men:
                    men = num
    print('La cantidad de numeros que terminan en 5 es: ', numeros5)
    print('El porcentaje de pares en la secuencia es de: ', porcentaje)
    print('El numero menor divisible por 3 es: ',men)
else:
    print('Ingrese un numero mayor que 0')