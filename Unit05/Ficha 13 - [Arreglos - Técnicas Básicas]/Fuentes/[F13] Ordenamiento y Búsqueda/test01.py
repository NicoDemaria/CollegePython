__author__ = 'Cátedra de AED'

import arreglos


def validate(inf):
    n = inf
    while n <= inf:
        n = int(input('Ingrese cantidad de elementos (mayor a ' + str(inf) + ' por favor): '))
        if n <= inf:
            print('Error: se pidio mayor a', inf, '... cargue de nuevo...')

    return n


def test():
    # cargar cantidad de elementos...
    n = validate(0)

    # crear un arreglo de n elementos (valor inicial 0)...
    v = n * [0]

    # cargar el arreglo por teclado...
    print('\nVector v:')
    arreglos.read(v)

    # ordenar el arreglo...
    arreglos.selection_sort(v)

    # mostrar el vector ordenado...
    print('\nEl vector ordenado es:', v)


# script principal...
if __name__ == '__main__':
    test()