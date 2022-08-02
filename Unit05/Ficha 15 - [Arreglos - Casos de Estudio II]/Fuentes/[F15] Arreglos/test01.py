__author__ = 'Cátedra de AED'


def validate(inf):
    n = inf
    while n <= inf:
        n = int(input('Ingrese cantidad de elementos (mayor a ' + str(inf) + ' por favor): '))
        if n <= inf:
            print('Error: se pidio mayor a', inf, '... cargue de nuevo...')

    return n


def read(alt):
    n = len(alt)
    print('Cargue ahora las alturas (en centimetros) del grupo...')
    for i in range(n):
        alt[i] = int(input('Altura[' + str(i) + ']: '))


def average(alt):
    n, s = len(alt), 0
    for i in range(n):
        s += alt[i]

    return s/n


def count(alt, med):
    n = len(alt)
    c1 = c2 = 0
    for i in range(n):
        if alt[i] > med:
            c1 += 1
        else:
            c2 += 1

    return c1, c2


def test():
    # cargar cantidad de personas...
    n = validate(0)

    # crear el arreglo de n elementos...
    alturas = n * [0]

    # cargar arreglo por teclado...
    read(alturas)

    # calcular el promedio y efecturar el conteo...
    media = average(alturas)
    mayores, menores = count(alturas, media)

    # mostras resultados...
    print('La altura media del grupo es:', media)
    print('Alturas mayores a la media:', mayores)
    print('Alturas menores a la media:', menores)


# script principal...
if __name__ == '__main__':
    test()

