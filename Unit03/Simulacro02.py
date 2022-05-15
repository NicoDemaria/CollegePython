#Desarrolle un programa completo en Python que permita generar una sucesión de 25000 números
# enteros aleatorios, usando como semilla del generador el número 20220512 (es decir random.seed(20220512)).
# Los valores de cada uno de esos 25000 números deben estar entre 1 y 50000 (incluidos ambos)
# (DEBE usar random.randint(1, 50000) para generar esos números). A partir de esa sucesión el programa debe:

#1. Determinar la cantidad de números múltiplos de 3 y también la cantidad de números múltiplos de 5 pero no de 3
# y finalmente la cantidad de números que no cumplen ninguna de las 2 condiciones.
#2.Indicar el mayor entre todos los números comienzan con el dígito 1, es decir 1234 comienza con 1 y
# 2345 no comienza con 1.
#3.Indicar el promedio entero truncado de los números generados que son pares y múltiplos de 11.
#4.Indicar el porcentaje entero que representa cada contador del punto 1.
# Aclaración 1: NO se pide el porcentaje redondeado, sino el porcentaje truncado, sin decimales.
# Aclaración 2: en el cálculo de este porcentaje, haga primero la multiplicación que corresponda, y
# luego la división.

import random
random.seed(20220512)
n = 25000
inicio = 1
fin = 50000
multiplos3 = 0
multiplos5 = 0
noMulti = 0
pares11 = 0
may = 0
truncar = 0
for i in range(n):
    num = random.randint(inicio, fin)

    # 1
    if num % 3 == 0:
        multiplos3 += 1
    else:
        if num % 5 == 0:
            multiplos5 += 1
        else:
            noMulti += 1

    # 2

    if num % 10 == 1:
        if i == 0:
            may = num
        elif num > may:
            may = num
    # 3

    if num % 2 == 0 and num % 11 == 0:
        truncar += num
        pares11 += 1

        promedio = truncar // pares11



    # 4

porcentaje3 = (multiplos3*100) // n
porcentaje5 = (multiplos5*100) // n
porcentajeNoMulti = (noMulti*100) // n


print(multiplos3,multiplos5,noMulti)

print(' el mayor numero es: ',may)

print('Promedio de pares multi de 11:', promedio,'%')

print(porcentaje3, porcentaje5, porcentajeNoMulti)



