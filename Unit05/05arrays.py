'''
1. Pluviómetro
Se ha solicitado un programa que permita cargar las precipitaciones promedio en cada mes del país, en base a esos datos armar un menú de opciones que permita:

Determinar el promedio anual de lluvias, 1
Determinar el promedio de lluvias para un determinado trimestre, 2
Determinar el mes más seco del año, 3
Determinar los meses del año en los que llovió más que el promedios de lluvia de todo el año., 4
'''
# notas = []
# for i in range(4):
#     x = int(input('Ingrese nota: '))
#     notas.append(x)
# print('Notas:', notas)
# suma = 0
# for i in range(4):
#     suma += notas[i]
#     promedio = suma / 4
# print('Promedio:', promedio)


from __future__ import print_function


def cargalluvias():
    lluvias = []
    for i in range(12):
        x = int(input('Ingrese la cantidad de precipitaciones: '))
        lluvias.append(x)
    return lluvias

# Opcion 1


def promedioAnual(lluviasanuales):
    total = 0
    meses = 12

    for i in range(len(lluviasanuales)):
        total += lluviasanuales[i]
    prom = total//meses
    return prom


def determinarTrimestre():


def main():
    lluviasanuales = cargalluvias()
    promedio = promedioAnual(lluviasanuales)

    return lluviasanuales


main()
