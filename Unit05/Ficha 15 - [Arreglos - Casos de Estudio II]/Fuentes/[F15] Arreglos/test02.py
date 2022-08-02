__author__ = 'Cátedra de AED'


def validate(inf):
    t = inf
    while t <= inf:
        t = int(input('Cantidad (mayor a ' + str(inf) + ' por favor): '))
        if t <= inf:
            print('Error: se pidio mayor a', inf, '... cargue de nuevo...')

    return t


def read(v):
    n = len(v)
    print('Cargue ahora los datos de este arreglo...')
    for i in range(n):
        v[i] = int(input('Valor[' + str(i) + ']: '))


def generate(v1, v2):
    v3 = []
    for i in range(len(v1)):

        # comprobar si v1[i] ya está en v3...
        exists = False
        for k in range(len(v3)):
            if v3[k] == v1[i]:
                exists = True
                break

        # si v1[i] no está en v3, buscarlo en v2...
        if not exists:
            for j in range(len(v2)):
                if v1[i] == v2[j]:
                    # si está también en v2  agregarlo en v3 y cortar el ciclo...
                    v3.append(v1[i])
                    break

    # retornar el nuevo arreglo...
    return v3


def test():
    # primer arreglo...
    print('Primer arreglo...')
    n = validate(0)
    v1 = n * [0]
    read(v1)
    print()

    # segundo arreglo...
    print('Segundo arreglo...')
    m = validate(0)
    v2 = m * [0]
    read(v2)
    print()

    # generar y mostrar el tercer arreglo...
    v3 = generate(v1, v2)
    print('Los valores presentes en ambos arreglos son:')
    print(v3)


if __name__ == '__main__':
    test()
