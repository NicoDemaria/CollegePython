__author__ = 'Cátedra de AED'


def lists_test():
    # una lista de 15 ceros...
    ceros = 15 * [0]
    print("Lista de 15 ceros: ", ceros)

    # crear una lista con n numeros del 1 al n...
    n = 10
    numeros = []
    for i in range(1, n+1):
        numeros.append(i)
    print('Lista original: ', numeros)

    # recorrer de izquierda a derecha y mostrar los numeros pares de la lista
    print('Valores pares contenidos en la lista: ', end=' ')
    for i in range(len(numeros)):
        if numeros[i] % 2 == 0:
            print(numeros[i], end=' ')

    # recorrer de derecha a izquierda y mostrar todos los numeros de la lista
    print('\nContenido de la lista, en forma invertida: ', end=' ')
    for i in range(-1, (-len(numeros) - 1), -1):
        print(numeros[i], end=" ")

    # obtener una sublista a partir de un rango de indices...
    nueva = numeros[1:4]
    print('\nNueva lista: ', nueva)

    # una copia a nivel de referencias (copia "superficial")...
    copia1 = numeros  # ambas variables apuntan a la misma lista...
    numeros[2] = -1
    print('Original: ', numeros)
    print('Copia 1: ', copia1)

    # una copia a nivel de valores (copia "profunda")...
    copia2 = numeros[:]  # cada variable apunta a una lista diferente...
    numeros[2] = -10
    print('Original: ', numeros)
    print('Copia 2: ', copia2)

    # eliminar un elemento...
    del numeros[4]
    print('Original, luego de eliminar el quinto elemento: ', numeros)

    # las siguientes instrucciones provocan un error...
    # del numeros
    # print(numeros)

    # operaciones varias con cortes de indices...
    lis = [47, 17, 14, 41, 37, 74, 48]
    print('\nLista de prueba:', lis)

    # reemplazar elementos en un rango...
    lis[2:5] = [10, 20, 30]
    print('Lista modificada 1:', lis)

    # eliminar elementos en un rango...
    lis[1:4] = []
    print('Lista modificada 2:', lis)

    # insertar un elemento... en este caso en la posicion 2...
    lis[2:2] = [90]
    print('Lista modificada 3:', lis)

    # inserta una copia de si misma al principio...
    lis[:0] = lis
    print('Lista modificada 4:', lis)

    # agregar un elemento al final, mediante un corte...
    lis[len(lis):] = [100]  # lis.append(100)
    print('Lista modificada 5:', lis)

    # agregar un elemento al final... con un metodo de la clase list...
    lis.append(200)
    print('Lista modificada 6:', lis)

    # copiar desde el casillero 2 hasta el ante-último...
    l1 = lis[2:-1]
    print('Sub-lista 1:', l1)

    # copiar dos veces el subrango entre 2 y 4...
    l2 = 2 * lis[2:5]
    print('Sub-lista 2:', l2)

    # concatenar dos listas...
    l3 = lis[:4] + [1, 2, 3]
    print('Sub-lista 3:', l3)

    # vaciar una lista...
    lis[:] = []
    print('Lista original vacía:', lis)


if __name__ == '__main__':
    lists_test()
