'''
1. Pluviómetro
Se ha solicitado un programa que permita cargar las precipitaciones promedio en cada mes del país, en base a esos datos armar un menú de opciones que permita:

Determinar el promedio anual de lluvias, 1
Determinar el promedio de lluvias para un determinado trimestre, 2
Determinar el mes más seco del año, 3
Determinar los meses del año en los que llovió más que el promedios de lluvia de todo el año., 4
'''


from __future__ import print_function


def cargalluvias():
    lluvias = [0] * 12
    for i in range(len(lluvias)):
        x = int(input('Ingrese la cantidad de precipitaciones: '))
        lluvias[i] = x
    return lluvias

# Opcion 1


def promedioAnual(lluviasanuales):
    total = 0
    meses = 12

    for i in range(len(lluviasanuales)):
        total += lluviasanuales[i]
    prom = total//meses
    return prom


def determinarTrimestre(lluviasanuales):
    trimestre1 = lluviasanuales[0:3]
    trimestre2 = lluviasanuales[3:6]
    trimestre3 = lluviasanuales[6:9]
    trimestre4 = lluviasanuales[9:]

    return trimestre1, trimestre2, trimestre3, trimestre4


def mesSeco(lluviasanuales):
    seco = min(lluviasanuales)
    return seco


def lluviaMayorProm(lluviasanuales, promedio):
    mesesHumedos = []
    for i in range(len(lluviasanuales)):
        if lluviasanuales[i] > promedio:
            mesesHumedos.append(i+1)
    return mesesHumedos


def main():
    x = int(input('Ingrese una opccion'))
    lluviasanuales = cargalluvias()
    while x != 5:
        if x == 1:
            promedio = promedioAnual(lluviasanuales)
            print(promedio)
        elif x == 2:
            opc = int(input('Ingrese el trimestre que desea: '))
            if opc == 1:
                print(selectri1)
            elif opc == 2:
                print(selectri2)
            elif opc == 3:
                print(selectri3)
            elif opc == 4:
                print(selectri4)

            selectri1, selectri2, selectri3, selectri4 = determinarTrimestre(
                lluviasanuales)

        mesMenosLluvias = mesSeco(lluviasanuales)
        punto4 = lluviaMayorProm(lluviasanuales, promedio)

    return lluviasanuales, promedio


main()
