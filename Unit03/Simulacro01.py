# Desarrolle un programa completo en Python que permita generar una sucesión de 20000 números enteros aleatorios, usando como semilla del generador el numero 49 (es decir random.seed(49)). Los valores de cada uno de esos 20000 números deben estar entre 1 y 45000 (incluidos ambos) (DEBE usar random.randint(1, 45000) para generar esos números). A partir de esa sucesión el programa debe:

# Indicar cuantos números eran múltiplos de 5, cuántos eran múltiplos de 7 y cuántos eran múltiplos de 9.
# Indicar el mayor entre todos aquellos números cuyo último dígito sea mayor o igual a 5 pero menor o igual a 8.
# Indicar cuantos números generados son pares menores a 15000.
# Indicar el porcentaje entero que representa el punto anterior sobre el total de números procesados. Aclaración 1: NO se pide el porcentaje redondeado, sino el porcentaje truncado, sin decimales. Aclaración 2: en el cálculo de este porcentaje, haga primero la multiplicación que corresponda, y luego la división.
# Cuando finalice, en las consignas que siguen en este mismo cuestionario, se le pedirá que informe cada uno de estos resultados, y también se le pedirá que suba el archivo de código fuente con el programa desarrollado (por lo que tenga muy presente en donde dejó ese archivo). Habrá también UNA pregunta de opciones múltiples referida a este mismo enunciado o a temas relacionados con él.

from os import truncate
import random
import math

random.seed(49)

n = 20000
inicio = 1
fin = 45000
multiplos5 = 0
multiplos7 = 0
multiplos9 = 0
multiplosPares = 0
may = 0
for i in range(n):
    num = random.randint(inicio, fin)
    # 1
    if num % 5 == 0:
        multiplos5 += 1
    if num % 7 == 0:
        multiplos7 += 1
    if num % 9 == 0:
        multiplos9 += 1
    # 2
    if num % 10 == 5 or num % 10 == 6 or num % 10 == 7 or num % 10 == 8:
        if i == 1:
            may = num
        elif num > may:
            may = num
    # 3
    if num % 2 == 0 and num < 15000:
        multiplosPares += 1
    # 4

    porcentaje = (multiplosPares*100) / n
    round(porcentaje, 0)

print('Punto 1:', multiplos5, multiplos7, multiplos9)
print('Punto 2:', may)
print('Punto 3:', multiplosPares)
print('Punto 4:', porcentaje)
