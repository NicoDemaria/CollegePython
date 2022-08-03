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

    # crear dos arreglos de n elementos (valor inicial 0)...
    a = n * [0]
    b = n * [0]

    # cargar los dos arreglos por teclado...
    print('\nVector a:')
    arreglos.read(a)

    print('\nVector b:')
    arreglos.read(b)

    # obtener el producto escalar...
    pe = arreglos.scalar_product(a, b)

    # mostrar el prodcuto escalar...
    print('\nEl producto escalar es:', pe)


# script principal...
if __name__ == '__main__':
    test()