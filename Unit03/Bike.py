# 1. Ciclistas
# La final de una carrera de ciclistas tiene n competidores (n se ingresa por teclado).

# Desarrollar un programa que permita cargar, por cada competidor, nombre y tiempo de carrera. Luego se pide:

# a) Determinar y mostrar el nombre del ganador de la carrera.

# b) Ingresar por teclado el tiempo record registrado para dicha carrera. Determinar si el tiempo del ganador es menor al tiempo record, mostrar un mensaje.

# c) Calcular y mostrar el tiempo promedio entre todos los ciclistas.


n = input("Ingrese la cantidad de competidores: ")
contador = 0
for i in range(int(n)):
    contador += int(tiempo)
    promedio = contador / int(n)

    print("Competidor ", i + 1)
    nombre = input("Ingrese el nombre del competidor: ")
    tiempo = input("Ingrese el tiempo del competidor(minutos): ")
    print("Nombre: ", nombre, " Tiempo: ", tiempo)

tiempoRecord = input("Ingrese el tiempo record: ")
if tiempo > tiempoRecord:
    print("El tiempo del competidor es mayor al tiempo record",
          tiempo, ">", tiempoRecord)
