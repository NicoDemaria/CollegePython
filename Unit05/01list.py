''''
Cargar por teclado un arreglo de n componentes y multiplicarlo por el valor k que también se ingresa por teclado.
'''


def main():
    invalido = True
    arr = []
    n = int(input('Ingrese la cantidad de componentes: '))
    if n <= 0:
        while invalido:
            n = int(input('Ingrese un num positivo: '))
            if n > 0:
                invalido = False

    k = int(input('Ingrese numero para multiplicar cada index:'))
    for i in range(n):
        num = int(input('Ingrese numero para agregar al array:'))

        arr.append(num * k)
    return arr


# print(main())


hola = main()
print(hola)


# main
