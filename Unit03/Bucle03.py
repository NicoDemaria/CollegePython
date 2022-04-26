# Ejercicio 3
# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.


n = int(input('Porfavor ingrese un numero entero y positivo: '))

for i in range(1, n+1, 2):
    print(i, end=',')
