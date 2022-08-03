"""Funciones elementales para manejo de arreglos unidimensionales
   representados mediante variables de tipo list en Python.
"""

__author__ = 'Cátedra de AED'


def read(v):
    # carga por teclado de un vector de n componentes...
    n = len(v)
    print('Cargue los elementos del vector:')
    for i in range(n):
        v[i] = int(input('casilla[' + str(i) + ']: '))


def add(a, b):
    # suma los arreglos a y b, y retorna el arreglo suma...
    n = len(a)
    c = n * [0]
    for i in range(n):
        c[i] = a[i] + b[i]

    return c


def product(v, k):
    # multiplica por k al arreglo y lo retorna...
    n = len(v)
    for i in range(n):
        v[i] *= k


def scalar_product(a, b):
    # calcula el producto escalar entre a y b...
    n = len(a)

    sp = 0
    for i in range(n):
        sp += a[i]*b[i]

    return sp
