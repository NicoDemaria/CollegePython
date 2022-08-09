'''
Desarrollar un programa que permita procesar el puntaje obtenido por una pareja de bailarines en un concurso de TV.

Para ello, generar un vector de 7 elementos, representando a los miembros del jurado. Por cada celda, generar un valor aleatorio entre -1 y 10 (inclusive) indicando la puntuación recibida.

A continuación, informar:

Los tres mejores puntajes recibidos. hecho
Si algún jurado los calificó con un puntaje x ingresado por teclado. En caso afirmativo, mostrar las notas mayores a esa que recibieron. hecho
La diferencia entre el mayor y el menor puntaje.
El puntaje total obtenido. Si es menor a 20, indicar que quedan descalificados. En caso contrario, informar como puntaje final el promedio de los puntos obtenidos, excluyendo los extremos.
'''

import random
from re import I
from traceback import print_tb
from xml.etree.ElementTree import XML


def generarJurado():
    jurados = [0] * 7
    n = len(jurados)
    for i in range(n):
        jurados[i] = random.randint(-1, 10)

    return jurados


def ordenarPuntos(jurados):
    n = len(jurados)
    for i in range(n):
        for j in range(i+1, n):
            if jurados[i] > jurados[j]:
                jurados[i], jurados[j] = jurados[j], jurados[i]
    return jurados


def busquedaPuntaje(puntajesOrdenados):
    existe = False
    x = int(input('Ingrese un puntaje a buscar(-1:10): '))
    for i in range(len(puntajesOrdenados)):
        if puntajesOrdenados[i] == x:
            existe = True
            print('El puntaje existe y es:', x)

    if existe == False:
        print('No se encontro el puntaje')


def dif(puntajesOrdenados):
    c = puntajesOrdenados[6] - puntajesOrdenados[0]
    return c


def main():
    jurados = generarJurado()
    puntajesOrdenados = ordenarPuntos(jurados)
    print(puntajesOrdenados)
    print('Los mejores puntajes fueron: ', puntajesOrdenados[4:7])
    busquedaPuntaje(puntajesOrdenados)
    c = dif(puntajesOrdenados)
    print('La diferencia entre el puntaje mas alto es de:', c, 'puntos')


main()
