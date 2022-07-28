'''
Cargar por teclado dos vectores de tamaño n y obtener el producto escalar de ambos.
'''

from array import array


def main(arr, arr1):
    n = len(arr)
    expresion = 0
    for i in range(n):
        expresion += arr[i] * arr1[i]
    return expresion


def vectores():
    invalido = True
    n = int(input('Ingrese la cantidad de componentes: '))

    if n <= 0:
        while invalido:
            n = int(input('Ingrese un num positivo: '))
            if n > 0:
                invalido = False
    arr = n * [0]
    arr1 = n * [0]
    for i in range(n):
        arr[i] = int(input('Ingrese el numero para agregar al primer v: '))

    for i in range(n):
        arr1[i] = int(input('Ingrese el numero para agregar al segundo v: '))
    return arr, arr1


a, b = vectores()
expresion = main(a, b)
print('El producto escalar entre los dos vectores es: ', expresion)
