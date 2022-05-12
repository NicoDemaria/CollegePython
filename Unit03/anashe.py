cant = int(input('Ingrese la cantidad de competidores: '))
time_ganador = 0
contadorProm = 0
for i in range(1, cant+1):
    name = str(input('Ingrese el nombre de el competidor: '))
    time = int(input('Ingrese el tiempo que realizo en minutos: '))

contadorProm += time
print('El nombre de el competidor es:', name, 'y su tiempo es:', time)
if i == 1:
    time_ganador = time
    name_ganador = name
else:
    if time < time_ganador:
        time_ganador = time
name_ganador = name


print('=========================================================')
promedio = contadorProm/cant
print('El promedio de tiempo entre los ciclistas es: ', promedio)
print('=========================================================')

print('=========================================================')
print('El ganador es: ', name_ganador, 'con un tiempo de:', time_ganador)
print('=========================================================')

timeRecord = int(input('Ingrese tiempo record: '))

if time_ganador < timeRecord:
    print('El tiempo record fue superado, es:', time_ganador)
else:
    print('El tiempo record no fue superado.')
