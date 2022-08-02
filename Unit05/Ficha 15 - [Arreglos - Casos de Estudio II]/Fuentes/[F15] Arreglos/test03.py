__author__ = 'Cátedra de AED'


def validate(inf):
    n = inf
    while n <= inf:
        n = int(input('Valor (mayor a ' + str(inf) + ' por favor): '))
        if n <= inf:
            print('Error: se pidio mayor a', inf, '... cargue de nuevo...')

    return n


def read(v):
    n = len(v)
    print('Cargue ahora los datos...')
    for i in range(n):
        v[i] = int(input('v[' + str(i) + ']: '))


def sequence(v, k):
    n = len(v)
    for i in range(1, n):
        if v[i] != v[i-1] + k:
            return False

    return True


def test():
    # cargar tamaño del arreglo...
    print('Ingrese tamaño del arreglo...')
    n = validate(0)
    print()

    # crear el arreglo de n elementos...
    v = n * [0]

    # cargar arreglo por teclado...
    read(v)
    print()

    # cargar el valor de k...
    print('Ingrese el valor de k...')
    k = validate(0)

    # comprobar la secuencia...
    ok = sequence(v, k)

    # mostras resultados...
    if ok:
        print('El arreglo está en secuencia de', k, 'en', k)
    else:
        print('El arreglo no está en secuencia de', k, 'en', k)


# script principal...
if __name__ == '__main__':
    test()
