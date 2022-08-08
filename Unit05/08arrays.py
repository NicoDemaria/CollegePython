'''
Cargar por teclado dos vectores de tamaño n y, a partir de ellos, generar un tercer vector que contenga, para cada componente, el mayor valor entre las componentes homólogas (mismo índice) de los otros dos vectores.

Por ejemplo, si se cargan los siguientes vectores a y b:

a = [3, 4, 6]

b = [8, 5, 1]

El resultado sería:

c = [8, 5, 6]'''


def validarVec():
    n = int(input('Ingrese el tamanio de los vectores: '))
    while n <= 0:
        n = int(input('Ingrese el tamanio de los vectores: '))
    return n


def cargarComponentes(n):
    v = []
    for i in range(n):
        num = int(input('Ingrese los elementos de el vector: '))
        v.append(num)
    return v


def comparador(a, b):
    c = [0] * len(a)
    for i in range(len(a)):
        if a[i] > b[i]:
            c[i] = a[i]
        else:
            c[i] = b[i]
    return c


def main():
    n = validarVec()
    a = cargarComponentes(n)
    b = cargarComponentes(n)
    c = comparador(a, b)
    print(c)


main()
