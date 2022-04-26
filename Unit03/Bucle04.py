# Ejercicio 4
# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

n = int(input('Porfavor ingrese un numero entero y positivo: '))


for i in range(1, n+1):
    n -= 1
    print(n, end=',')
