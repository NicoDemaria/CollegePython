# 3. Sueldos y aguinaldo
# Ingresar por teclado los sueldos de un vendedor, correspondientes al primer semestre del año y luego:

# a) Calcular su aguinaldo, sabiendo que es la mitad del sueldo más alto del período.

# b) Determinar en qué mes recibió el sueldo más bajo del período.

# c) Informar el sueldo promedio del semestre.

semestre = 6

sumatoriaSueldo = 0

for i in range(semestre):

    sueldo = int(input('Ingrese el sueldo de los meses: '))
    sumatoriaSueldo += sueldo
    print(sumatoriaSueldo)
