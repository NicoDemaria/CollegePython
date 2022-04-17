# Problema 15.) Cargar por teclado una lista de números enteros que irán llegando uno a uno, y que representan cantidades mensuales de automóviles nuevos vendidos en el país durante cierto período. Para indicar que la carga de datos debe finalizar, se ingresará el valor -1 (menos uno) (note que el valor 0 (cero) puede ser un dato valido: es perfectamente posible que no haya habido ventas en un mes determinado). Se pide:
# a. Determinar cuántas de esas cantidades fueron mayores o iguales que 0 pero menores que 10000 unidades, cuántas fueron mayores o iguales a 10000 pero menores que 15000, y cuántas fueron mayores o iguales que 15000.
# b. Determinar la cantidad total de automóviles nuevos que se vendieron en el país.
# c. Determinar si se ingresó al menos una cantidad igual a 0 o no. Informe con un mensaje simple en pantalla.


c1, c2, c3, t = 0, 0, 0, 0
ok = False

cant = int(
    input('Ingrese la cantidad de autos vendidos(con -1 termina el programa): '))

# PUNTO A
while cant != -1:
    if c1 >= 0 and c1 <= 10000:
        print('Se vendieron la siguiente cantidad de autos en el primer intervalo de ventas:', c1)
    elif c2 >= 10000 and c2 <= 15000:
        print('Se vendieron la siguiente cantidad de autos en el segundo intervalo de ventas:', c2)
    elif c3 >= 15000:
        print('Se vendieron la siguiente cantidad de autos en el tercer intervalo de ventas:', c3)


t += cant
print(cant)
