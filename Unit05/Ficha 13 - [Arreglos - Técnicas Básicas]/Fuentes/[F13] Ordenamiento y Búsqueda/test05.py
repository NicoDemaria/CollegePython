__author__ = 'Cátedra de AED'

import arreglos


def validate(inf):
    n = inf
    while n <= inf:
        n = int(input('Ingrese cantidad de elementos (mayor a ' + str(inf) + ' por favor): '))
        if n <= inf:
            print('Error: se pidio mayor a', inf, '... cargue de nuevo...')

    return n


def generate(v, factor=3):
    # carga el arreglo con una secuencia ordenada simple...
    n = len(v)
    for i in range(n):
        v[i] = factor*i


def test():
    # generar el primer vector...
    print('Vector a:')
    n = validate(0)
    a = n * [0]
    generate(a, 2)

    # generar el segundo vector...
    print('\nVector b:')
    m = validate(0)
    b = m * [0]
    generate(b, 5)

    # fusionar y obtener el tercer vector ordenado...
    c = arreglos.merge(a, b)

    # mostrar el vector fusionado...
    print()
    print('El primer vector es:', a)
    print('El segundo vector es:', b)
    print('El vector fusionado es:', c)

# script principal...
if __name__ == '__main__':
    test()
