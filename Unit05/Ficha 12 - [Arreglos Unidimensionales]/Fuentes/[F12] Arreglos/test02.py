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
    arreglos.read(v)

    # cargar el número k por el cual se multiplicará al vector...
    k = int(input('Ingrese el valor de k: '))

    # multiplicar el vector por k...
    arreglos.product(v, k)

    # mostrar el vector final...
    print('El vector quedó así:', v)


# script principal...
if __name__ == '__main__':
    test()
