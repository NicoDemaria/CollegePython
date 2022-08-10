'''
1. Estudio climatológico
Como parte de un estudio climatológico, se desea un programa que permita obtener una serie de estadísticas a partir de un conjunto de muestras de temperatura.

Se pide un programa que:

Ingrese n muestras de temperatura, donde cada muestra contiene la temperatura registrada, la región donde se registró la misma (1-20), y el día del mes en el que se registró la temperatura 1
Determinar el promedio general de temperatura  2
Dada una región, mostrar las temperaturas de la misma, ordenadas por dia, de menor a mayor 3
Dada una región, determinar si la temperatura de alguna muestra superó el valor x, ingresado por teclado. 4
Determinar la cantidad de muestras por region (20 contadores) 5
'''


import re


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


def ordenar(temperaturas, regiones, dias, n):
    for i in range(n):
        for j in range(i+1, n):
            if dias[i] > dias[j]:
                dias[i], dias[j] = dias[j], dias[i]
                regiones[i], regiones[j] = regiones[j], regiones[i]
                temperaturas[i], temperaturas[j] = temperaturas[j], temperaturas[i]


def mostrar_temperaturas(dias, regiones, temperaturas, reg):
    print("Dia \t\t Temperatura")
    for i in range(len(regiones)):
        if regiones[i] == reg:
            print(dias[i], "\t\t\t", temperaturas[i])


def buscarTempReg(temperaturas, regiones, reg, x):
    existe = False
    for i in range(len(regiones)):
        if reg == regiones[i] and x < temperaturas[i]:
            existe = True
    return existe


def main():
    opc = 0
    while opc != 6:
        opc = int(input('Ingrese la opcion deseada(6 termina): '))
        if opc == 1:
            temperaturas, regiones, dias, n = cargaDatos()
        elif opc == 2:
            promedioTemp = promTemp(temperaturas, n)
            print('El promedio de temperaturas es: ', promedioTemp)
        elif opc == 3:
            ordenar(temperaturas, regiones, dias, n)
            reg = int(input("Ingrese región a analizar: "))
            mostrar_temperaturas(dias, regiones, temperaturas, reg)
        elif opc == 4:
            reg = int(input('Ingrese region: '))
            x = int(input('Ingrese temperatura a buscar: '))
            existe = buscarTempReg(temperaturas, regiones, reg, x)
            if existe:
                print('Existe al menos una temperatura mayor a: ',
                      x, 'en la region', reg)
            else:
                print('No existe esa temperatura en la region seleccionada')

        elif opc == 6:
            print('Hasta la proximaaaa ')
        else:
            print('Ingrese un numero valido')


main()
