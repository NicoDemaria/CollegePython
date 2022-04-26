# 2. Secuencia de impares
# Cargar por teclado dos números, e imprimir los números impares que se encuentran comprendidos entre ellos, en forma ascendente y descendente.
n1 = int(input("Ingrese el primer número(entero y positivo): "))
n2 = int(input("Ingrese el segundo número(mayor que num1): "))


if n2 < n1:
    print('Le dije que ingresara un numero mayor que el primero:' + str(n1))
else:
    for i in range(n1, n2 + 1):
        if i % 2 != 0:
            print(i)
