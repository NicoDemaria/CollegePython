# 1. Ciclistas
# La final de una carrera de ciclistas tiene n competidores (n se ingresa por teclado).

# A un programa que permita cargar, por cada competidor, nombre y tiempo de carrera. Luego se pide:

# a) Determinar y mostrar el nombre del ganador de la carrera.

# Ab) Ingresar por teclado el tiempo record registrado para dicha carrera. Determinar si el tiempo del ganador es menor al tiempo record, mostrar un mensaje.

# Ac) Calcular y mostrar el tiempo promedio entre todos los ciclistas.


cant = int(input('Ingrese la cantidad de competidores: '))
contadorProm = 0
for i in range(1, cant+1):
    name = str(input('Ingrese el nombre de el competidor: '))
    time = int(input('Ingrese el tiempo que realizo en minutos: '))
    contadorProm += time
    print('El nombre de el competidor es:',name,'y su tiempo es:',time)
    if i == 1:
        mayor = time
    else:
        if time > mayor :
            mayor = time
print('=========================================================')
promedio = contadorProm/cant
print('El promedio de tiempo entre los ciclistas es: ', promedio)
print('=========================================================')

print('=========================================================')
print('El ganador es: ',mayor, name)
print('=========================================================')

timeRecord = int(input('Ingrese tiempo record: '))

if mayor < timeRecord:
    print('El tiempo record fue superado,', mayor)
else:
    print('El tiempo record no fue superado.')
