# Se pide desarrollar un programa en python que cargue por teclado un numero n y calcule muestre su factorial (n!).


n = int(input("Ingrese un numero: "))
multiplicador = 1
for i in range(1, n + 1):
    multiplicador *= i
    # print('n!: ', multiplicador)

print('El factorial de', n, 'es: ', multiplicador)
