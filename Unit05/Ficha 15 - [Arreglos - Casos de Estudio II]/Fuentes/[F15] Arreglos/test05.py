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


def search(alturas, x):
    n = len(alturas)
    for i in range(n):
        if x == alturas[i]:
            return i
    return -1


def sort(alturas):
    n = len(alturas)
    for i in range(n-1):
        for j in range(i+1, n):
            if alturas[i] > alturas[j]:
                alturas[i], alturas[j] = alturas[j], alturas[i]


def test():
    # el arreglo comienza vacio
    alturas = []

    # menú de opciones...
    op = -1
    while op != 6:
        # mostrar el menú...
        print("Programa de gestión de alturas...")
        print("1. Cargar el arreglo.")
        print("2. Mostrar el arreglo.")
        print("3. Contar mayores y menores a la media.")
        print("4. Buscar una altura.")
        print("5. Ordenar de menor a mayor.")
        print("6. Terminar y salir.")
        op = int(input("Ingrese el número de la opción elegida: "))
        print()

        if op == 1:
            # cargar el arreglo...
            n = validate(0)
            alturas = n * [0]
            read(alturas)
            print()

        elif op == 2:
            # controlar si el arreglo fue efectivamente cargado...
            if len(alturas) != 0:
                print("Las alturas cargadas son:", alturas)
            else:
                print("No hay datos cargados en el arreglo...")
            print()

        elif op == 3:
            # controlar si el arreglo fue efectivamente cargado...
            if len(alturas) != 0:
                # calcular el promedio y efectuar el conteo...
                media = average(alturas)
                mayores, menores = count(alturas, media)
                print('La altura media del grupo es:', media)
                print('Alturas mayores a la media:', mayores)
                print('Alturas menores a la media:', menores)
            else:
                print("No hay datos cargados en el arreglo...")
            print()

        elif op == 4:
            # controlar si el arreglo fue efectivamente cargado...
            if len(alturas) != 0:
                # cargar y buscar una altura...
                x = int(input("Altura a buscar: "))
                pos = search(alturas, x)
                if pos >= 0:
                    print("Está en la casilla", pos)
                else:
                    print("No está en el arreglo")
            else:
                print("No hay datos cargados en el arreglo...")
            print()

        elif op == 5:
            # controlar si el arreglo fue efectivamente cargado...
            if len(alturas) != 0:
                # ordenar...
                sort(alturas)
                print("Hecho. El arreglo fue ordenado de menor a mayor.")
            else:
                print("No hay datos cargados en el arreglo...")
            print()


# script principal...
if __name__ == '__main__':
    test()
