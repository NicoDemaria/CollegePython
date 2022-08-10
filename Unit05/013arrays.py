'''
1. Estudio climatológico
Como parte de un estudio climatológico, se desea un programa que permita obtener una serie de estadísticas a partir de un conjunto de muestras de temperatura.

Se pide un programa que:

Ingrese n muestras de temperatura, donde cada muestra contiene la temperatura registrada, la región donde se registró la misma (1-20), y el día del mes en el que se registró la temperatura
Determinar el promedio general de temperatura  1 
Dada una región, mostrar las temperaturas de la misma, ordenadas por dia, de menor a mayor 2 
Dada una región, determinar si la temperatura de alguna muestra superó el valor x, ingresado por teclado. 3 
Determinar la cantidad de muestras por region (20 contadores) 4
'''


def cargaDatos():
    n = int(input('Ingrese la cantidad de temperaturas a registrar: '))
    temperaturas = [0] * n
    regiones = [0] * n
    dias = [0] * n
    while n < 1:
        n = int(input('Ingrese la cantidad de temperaturas a registrar: '))
    for i in range(n):
        temperatura = int(
            input('Ingrese la temp:  '))
        region = int(
            input('Ingrese la region a registrar(1:20): '))
        dia = int(input('Ingrese el dia de la temp: '))
        temperaturas[i] = temperatura
        regiones[i] = region
        dias[i] = dia
    return temperaturas, regiones, dias, n


def promTemp(temperaturas, n):
    total = 0
    for i in range(n):
        total += temperaturas[i]
    return total/n


def main():
    temperaturas, regiones, dias, n = cargaDatos()
    opc = 0
    while opc != 5:
        opc = int(input('Ingrese la opcion deseada(5 termina): '))
        if opc == 1:
            promedioTemp = promTemp(temperaturas, n)
            print('El promedio de temperaturas es: ', promedioTemp)
        elif opc == 2:
            pass
        elif opc == 5:
            print('Hasta la proximaaaa')
        else:
            print('Ingrese un numero valido')


main()
