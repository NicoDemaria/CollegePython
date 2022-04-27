# 3. Sueldos y aguinaldo
# Ingresar por teclado los sueldos de un vendedor, correspondientes al primer semestre del año y luego:

# a) Calcular su aguinaldo, sabiendo que es la mitad del sueldo más alto del período. =========

# b) Determinar en qué mes recibió el sueldo más bajo del período. =========

# c) Informar el sueldo promedio del semestre. =========

semestre = 6
sumatoriaSueldo = 0

for i in range(1, semestre+1):
    sueldo = int(input('Ingrese el sueldo de el mes: '))
    sumatoriaSueldo += sueldo
    promedioSueldo = sumatoriaSueldo/semestre

    # punto a, aguinaldo
    if i == 1:
        sueldoMay = sueldo
    else:
        if sueldo > sueldoMay:
            sueldoMay = sueldo
#Sueldo minimo
    if i == 1:
        sueldoMen = sueldo
    else:
        if sueldo < sueldoMen:
            sueldoMen = sueldo

print('El sueldo menor es: ',sueldoMen)



#sueldo mayor
print('El sueldo mayor de todo el semestre fue: ',sueldoMay)
#Aguinaldo
print('Su aguinaldo es:',sueldoMay/2)


#promedio de el sueldo
print('El promedio de su sueldo es: ',promedioSueldo)