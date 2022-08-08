'''Se pide un programa que cargue n elementos numéricos aleatorios entre 1 y 100 inclusive (pueden existir duplicados). A partir de ese arreglo:

Ordenarlo de forma ascendente y mostrarlo
Buscar un elemento x dentro del arreglo (x se ingresa por teclado). Si no existe, informarlo. Si existe, determinar cuántos valores impares mayores a x se encontraron en el arreglo.'''


import random


def validate(inf):
    n = inf
    while n <= inf:
        n = int(
            input('Ingrese cantidad de elementos (mayor a ' + str(inf) + ' por favor): '))
        if n <= inf:
            print('Error: se pidio mayor a', inf, '... cargue de nuevo...')

    return n


def cargaDatos():
    n = validate(0)
    v = n * [0]
    for i in range(n):
        v[i] = random.randint(1, 100)
    return v


def ordenar(v):
    n = len(v)
    for i in range(n):
        for j in range(i + 1, n):
            if v[i] > v[j]:
                v[i], v[j] = v[j], v[i]
    return v


def buscadorNum(v):
    contador = 0
    x = int(input('Ingrse el numero a buscar:'))
    for i in range(len(v)):
        if v[i] % 2 != 0 and v[i] > x:
            contador += 1
    return contador


def main():
    v = cargaDatos()
    vectorOrdenado = ordenar(v)
    print('El vector ordenado es:', vectorOrdenado)
    contadorNumeroBuscado = buscadorNum(vectorOrdenado)
    print(contadorNumeroBuscado)


main()
