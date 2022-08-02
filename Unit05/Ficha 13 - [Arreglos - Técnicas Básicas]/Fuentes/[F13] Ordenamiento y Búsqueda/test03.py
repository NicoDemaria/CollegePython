__author__ = 'Cátedra de AED'

import arreglos


def validate(inf):
    n = inf
    while n <= inf:
        n = int(input('Ingrese cantidad de elementos (mayor a ' + str(inf) + ' por favor): '))
        if n <= inf:
            print('Error: se pidio mayor a', inf, '... cargue de nuevo...')

    return n


def generate(v):
    # carga el arreglo con una secuencia ordenada simple...
    n = len(v)
    for i in range(n):
        v[i] = 3*i


def test():
    # cargar cantidad de elementos...
    n = validate(0)

    # crear un arreglo de n elementos (valor inicial 0)...
    v = n * [0]

    # generar el arreglo ordenado...
    generate(v)
    print('\nEl vector v fue creado con los siguientes valores:')
    print(v)

    x = int(input('\nValor a buscar en el arrreglo: '))

    # aplicar búsqueda secuencial...
    ind = arreglos.binary_search(v, x)

    # avisar por pantalla el resultado de la búsqueda...
    if ind >= 0:
        print('\nEstá en la casilla', ind)
    else:
        print('\nNo está en el arreglo')


# script principal...
if __name__ == '__main__':
    test()
