__author__ = 'Cátedra de AED'


def lists_test():
    # crear una lista con n numeros del 1 al n...
    n = 10
    numeros = [i for i in range(1, n+1)]
    print('Lista original:', numeros)

    # una lista con los cubos de los 10 primeros numeros...
    cubos = [i ** 3 for i in range(1, 11)]
    print('Lista de cubos:', cubos)

    # obtener una lista de tuplas (x, y) con (x in v1) and (y in v2) and (x < y)...
    # ...sin aplicar comprensión, sería...
    v1 = [7, 3, 4, 8]
    v2 = [1, 3, 5, 9]
    pares = []
    for x in v1:
        for y in v2:
            if x < y:
                pares.append((x, y))
    print('Pares formados:', pares)

    # obtener una lista de tuplas (x, y) con (x in v1) and (y in v2) and (x < y)...
    # ...por comprensión, sería...
    v1 = [7, 3, 4, 8]
    v2 = [1, 3, 5, 9]
    pares = [(x, y) for x in v1 for y in v2 if x < y]
    print('Pares formados:', pares)


if __name__ == '__main__':
    lists_test()
