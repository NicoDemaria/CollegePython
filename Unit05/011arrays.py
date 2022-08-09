'''Ingresar (o generar de manera aleatoria) los legajos de los n alumnos de un curso, siendo n un valor que se carga por teclado, y almacenarlos en un arreglo unidimensional. Se pide para ello:

a - Ordenar el arreglo de menor a mayor. Mostrar por pantalla como quedó.

b - Buscar en el arreglo el alumno con el legajo x, x se ingresa por teclado. Si existe mostrarlo, si no mostrar un mensaje de error.'''


import random
from tkinter import N


def validarN():
    n = int(input('Ingrese el n de alumnos: '))
    while n < 1:
        n = int(input('Ingrese el n de alumnos: '))
    return n


def generarLeg(num):
    legajos = [0] * num
    for i in range(len(legajos)):
        legajos[i] = random.randint(1, 100000)
    return legajos


def ordenarLeg(legajos):
    n = len(legajos)
    for i in range(n):
        for j in range(i+1, n):
            if legajos[i] > legajos[j]:
                legajos[i], legajos[j] = legajos[j], legajos[i]
    return legajos


def buscaLegajo(legajosOrdenados):
    n = len(legajosOrdenados)
    x = int(input('Ingrese un legajo a buscar(entre 0 y 10000): '))
    for i in range(n):
        if legajosOrdenados[i] == x:
            print('El legajo', x, 'esta adentro de el arreglo')
            break
        else:
            print('No se encontro el legajo deseado')
            break


89591


def main():
    num = validarN()
    legajos = generarLeg(num)
    legajosOrdenados = ordenarLeg(legajos)
    print('Los legajos ordenados son: ', legajosOrdenados)
    buscaLegajo(legajosOrdenados)


main()
