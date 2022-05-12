# 1. Secuencia numérica
# Ingresar una secuencia de números, de a uno por vez, la carga finaliza cuando el usuario ingresa el cero. Determinar
#
# a) Porcentaje que representan los números divisibles por 3 sobre el total de números ingresados en la secuencia
#
# b) Determinar la cantidad de números que son el cuadrado del número anterior
# c) Determinar la posición del mayor elemento impar de la secuencia

acumuladorDivisibles3 = -1
acumulador = -1
num = -1
cantCuadrados = 0


while num != 0:
    acumulador += 1
    num = int(input('Ingrese una secuencia de numeros( termina cuando ingrese 0): '))
    if (num % 3) == 0:
        acumuladorDivisibles3 += 1

    anterior1 = num
    if (anterior1 ** 2) == num:
        cantCuadrados += 1
prom = (acumuladorDivisibles3 / acumulador) * 100

print(acumuladorDivisibles3)
print(acumulador)
print(prom, '%')
print('Punto b respuesta: ', cantCuadrados)
