# 1. Simulacro - Divisibles por 4
# Desarrolle un programa que permita generar una sucesión de mil números enteros aleatorios, usando como semilla del generador al valor 11. Los números generados deben estar entre 1 y 2500 (ambos incluidos). A partir de esa sucesión, el programa debe informar:
#
# Cuántos números eran divisibles por 4 pero no por 8, y cuántos eran divisibles por ambos
# El promedio de los valores mayores a 2000
# Cuántos números eran menores al primer valor generado y qué porcentaje representan sobre el total de números
# Si alguna vez aparecieron en la secuencia los valores extremos del intervalo (1, 2500)


import random

random.seed(11)

divisibles4 = 0
divisiblesAmbos = 0
extremo = False
n = 1000
a =0
menores = 0
mayores2000 = 0
#Generacion de los 1000 numeros


for i in range(n):
    num = random.randint(1,2500)
    # divisibles por 4 y por ambos
    if num % 4 == 0:
        if num % 8 == 0:
            divisiblesAmbos +=1
        else:
            divisibles4 +=1
    # Promedio de numeros mayores a 2000
    if num >= 2000:
        mayores2000 =+1
        a =+ num
        prom = a/mayores2000
    #Cuantos son menos al primer valor generado y su promedio
    if i == 0:
        men = num
    elif men > num:
        menores =+ 1
        porcentajeMen = (100*menores) / n

    #Si aparece 1 o 2500 en la secuencia
if num == 1:
    extremo = True
elif num == 2500:
    extremo == True
if extremo == True:
    print('Hay extremos')
else:
    print('No hay ')






print('Los divisibles por 4 son: ',divisibles4)
print('Los divisibles por ambos: ',divisiblesAmbos)
print('El promedio de mayores a 2000 es: ',prom)
print('El porcentaje de numeros mayores al primero generado es:', porcentajeMen)









