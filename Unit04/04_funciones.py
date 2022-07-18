'''
Programa que calcula la tabla de multiplicar de cualquier numero entero dado por el usuario 
debe calcular de 0 a 12
'''
numero = int(input('Ingrese un numero:'))


def multiplicar(n1, n2):
    return str(n1) + ' * ' + str(n2) + ' = ' + str(n1*n2)


for i in range(0, 13):
    print(multiplicar(numero, i))
