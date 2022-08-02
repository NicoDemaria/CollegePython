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

    return v


def scalar_product(a, b):
    # calcula el producto escalar entre a y b...
    n = len(a)

    sp = 0
    for i in range(n):
        sp += a[i] * b[i]

    return sp


# busqueda binaria...
# ...asume arreglo ordenado...
def binary_search(v, x):
    n = len(v)
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if x == v[c]:
            return c
        if x < v[c]:
            der = c - 1
        else:
            izq = c + 1
    return -1


# busqueda secuencial...
def linear_search(v, x):
    n = len(v)
    for i in range(n):
        if x == v[i]:
            return i
    return -1


def selection_sort(v):
    # ordenamiento por seleccion directa
    n = len(v)
    for i in range(n-1):
        for j in range(i+1, n):
            if v[i] > v[j]:
                v[i], v[j] = v[j], v[i]


def merge(a, b):
    # crear el tercer arreglo con lugar para n + m elementos...
    n, m = len(a), len(b)
    t = n + m
    c = t * [0]

    # aplicar proceso de fusión...
    i = k = j = 0
    while i < n and j < m:
        if a[i] < b[j]:
            c[k] = a[i]
            i += 1
        else:
            c[k] = b[j]
            j += 1

        k += 1

    # determinar cuál de los vectores (a o b) terminó primero...
    # ... apuntar con v al otro...
    v, pos = b, j
    if i < n:
        v, pos = a, i

    # copiar en el vector de salida todos los valores que
    # quedaban en el vector v...
    while pos < len(v):
        c[k] = v[pos]
        pos += 1
        k += 1

    # retornar el vector fusionado...
    return c
