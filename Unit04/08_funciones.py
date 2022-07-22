'''Programa que pide dos numeros al usuario y realiza difrentes operaciones matematicas'''


print('Bienvenido al programa de calculadora')

print('------------------------------------------------------------')
print('1 para sumar')
print('2 para restar')
print('3 para multiplicar')
print('4 para dividir')
print('5 para potencia')
print('6 para raiz')
opcion = int(input('Ingrese la opcion que desea realizar: '))

print('------------------------------------------------------------')
n1 = float(input('Ingrese el primer numero para realizar las operaciones: '))
n2 = float(input('Ingrese el segundo numero para realizar las operaciones'))
print('------------------------------------------------------------')


def suma(n1, n2):
    return n1 + n2


def resta(n1, n2):
    return n1 - n2


def multiplicacion(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


def potencia(n1, n2):
    return n1 ** n2


def raiz(n1, n2):
    return n1 ** (1/n2)


# Scrip principal
if opcion == 1:
    print('La suma de los numeros es: ', suma(n1, n2))
elif opcion == 2:
    print('La resta de los numeros es: ', resta(n1, n2))
elif opcion == 3:
    print('La multiplicacion de los numeros es: ', multiplicacion(n1, n2))
elif opcion == 4:
    print('La division de los numeros es: ', division(n1, n2))
elif opcion == 5:
    print('La potencia de los numeros es: ', potencia(n1, n2))
elif opcion == 6:
    print('La raiz de los numeros es: ', raiz(n1, n2))
