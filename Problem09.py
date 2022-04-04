#  Problema 9.) Cargar por teclado tres números enteros. Determinar si el primero que se cargó es el mayor de los tres (informe en pantalla con un mensaje tal como: Es el mayor o No es el mayor).

n1, n2, n3 = input('Please, enter three numbers: ').split()


def mayor(n1, n2, n3):
    if n1 > n2 > n3:
        print('The first number is higher than n2 and n3', n1)
    else:
        print('The n2 and n3 are higher than n1', n2, n3)


print(mayor(n1, n2, n3))
