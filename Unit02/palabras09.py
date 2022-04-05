# 6. Analisis de palabra
# Se pide un programa que le solicite al usuario que ingrese una palabra. Con esa palabra calcular los siguientes puntos:

# Determinar la cantidad de letras que tiene  la palabra.
# Mostrar un mensaje que informe si la palabra termina en vocal.


p1 = str(input('Ingrese una palabra: '))


print('La palabra tiene la siguiente cantidad de caracteres: ', len(p1), '\n ')

if p1[-1] == 'a' or p1[-1] == 'e' or p1[-1] == 'i' or p1[-1] == 'o' or p1[-1] == 'u':
    print('La palabra termina con vocal', p1[-1])
