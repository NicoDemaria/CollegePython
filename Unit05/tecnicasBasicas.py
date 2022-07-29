i = 0
n = 0
# TODO ordenadar un arreglo de mayor a menor
for j in range(i+1, n):
    v = []
    if v[i] > v[j]:
        v[i], v[j] = v[j], v[i]


def selection_sort(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i+1, n):
            if v[i] > v[j]:
                v[i], v[j] = v[j], v[i]

# TODO búsqueda secuencial


def linear_search(v, x):
    for i in range(len(v)):
        if x == v[i]:
            return i

    return -1

# TODO Busqueda Binaria


def binary_search(v, x):
    # busqueda binaria... asume arreglo ordenado...
    izq, der = 0, len(v) - 1
    while izq <= der:
        c = (izq + der) // 2
        if x == v[c]:
            return c
        if x < v[c]:
            der = c - 1
        else:
            izq = c + 1
    return -1

# TODO Fusión de arreglos ordenados.
