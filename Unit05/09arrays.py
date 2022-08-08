'''
Mayores al promedio
Ingresar por teclado un arreglo unidimensional de números enteros de tamaño n, siendo n una variable que se ingresa por teclado. Se pide:

Calcular el valor promedio entre los números ingresados en el vector.
Determinar la cantidad de números del vector que son mayores al promedio.'''


def tamanio():
    n = int(input('Ingrese el tamaño del arreglo: '))
    while n < 1:
        n = int(input('Ingrese el tamaño del arreglo: '))
    return n


def cargaDatos(n):
    vector = []
    for i in range(n):
        vector.append(int(input('Ingrese un numero: ')))
    return vector


def promedio(vector, n):
    total = 0
    for i in range(n):
        total += vector[i]
    promedio = total / n
    return promedio


def mayoresPromedio(vector, n, promedio):
    mayores = 0
    for i in range(n):
        if vector[i] > promedio:
            mayores += 1
    return mayores


def main():
    n = tamanio()
    vector = cargaDatos(n)
    promedio1 = promedio(vector, n)
    mayores = mayoresPromedio(vector, n, promedio1)
    print('El promedio es: ', promedio1)
    print('La cantidad de numeros mayores al promedio es: ', mayores)


main()
