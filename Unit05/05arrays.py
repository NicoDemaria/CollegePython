'''
1. Pluviómetro
Se ha solicitado un programa que permita cargar las precipitaciones promedio en cada mes del país, en base a esos datos armar un menú de opciones que permita:

Determinar el promedio anual de lluvias, 1
Determinar el promedio de lluvias para un determinado trimestre, 2
Determinar el mes más seco del año, 3
Determinar los meses del año en los que llovió más que el promedios de lluvia de todo el año., 4
'''


def cargalluvias():
    lluvias = [0] * 12
    for i in range(len(lluvias)):
        print(i+1)
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


def determinarTrimestre(lluviasanuales, opc):
    sumador = 0

    if opc == 1:
        trimestre = lluviasanuales[0:3]

    elif opc == 2:
        trimestre = lluviasanuales[3:6]
    elif opc == 3:
        trimestre = lluviasanuales[6:9]
    elif opc == 4:
        trimestre = lluviasanuales[9:]
    for i in range(len(trimestre)):
        sumador += trimestre[i]
    prom = sumador/len(trimestre)
    return prom


def mesSeco(lluviasanuales):
    min = 0
    for i in range(len(lluviasanuales)):
        if lluviasanuales[i] < lluviasanuales[min]:
            min = i
    return min


def lluviaMayorProm(lluviasanuales, promedio):
    mesesHumedos = []
    for i in range(len(lluviasanuales)):
        if lluviasanuales[i] > promedio:
            mesesHumedos.append(i+1)
    return mesesHumedos


def main():
    lluviasanuales = cargalluvias()
    print('''
Determinar el promedio anual de lluvias, 1
Determinar el promedio de lluvias para un determinado trimestre, 2
Determinar el mes más seco del año, 3
Determinar los meses del año en los que llovió más que el promedios de lluvia de todo el año., 4
''')
    x = 0
    while x != 5:
        x = int(input('Ingrese una opcion: '))

        if x == 1:
            promedio = promedioAnual(lluviasanuales)
            print(promedio)
            pass
        elif x == 2:
            opc = int(input('Ingrese el trimestre que desea: '))
            tri = determinarTrimestre(lluviasanuales, opc)
            print(tri)
        elif x == 3:
            mesMenosLluvias = mesSeco(lluviasanuales)

            print(mesMenosLluvias)
        elif x == 4:
            promedio = promedioAnual(lluviasanuales)

            punto4 = lluviaMayorProm(lluviasanuales, promedio)

            print(punto4)
        elif x == 5:
            print('Hasta la proximaaaa :c ')
        else:
            print('Ingrese una opcion valida')

    return lluviasanuales, promedio


main()
