'''
1. Pluviómetro
Se ha solicitado un programa que permita cargar las precipitaciones promedio en cada mes del país, en base a esos datos armar un menú de opciones que permita:

Determinar el promedio anual de lluvias, 1
Determinar el promedio de lluvias para un determinado trimestre, 2
Determinar el mes más seco del año, 3
Determinar los meses del año en los que llovió más que el promedios de lluvia de todo el año., 4
'''


def promedioAnualluvias(lluvias):
    for i in lluvias:
        total += i
        promedio = total // 12
    return promedio


def main():
    lluvia = []
    meses = 12

    for i in range(meses):
        print('Mes: ', i+1)
        mensual = input('Ingrese la precipitacion promedio de el mes: ')
        lluvia.append(mensual)

    print('Determinar el promedio anual de lluvias, 1 ')
    print('Determinar el promedio de lluvias para un determinado trimestre, 2')
    print('Determinar el mes más seco del año, 3')
    print('Determinar los meses del año en los que llovió más que el promedios de lluvia de todo el año., 4')
    opccion = str(
        input('Ingrese una opcion porfavor, con 0 se termina el programa'))
    while opccion != 0:
        if opccion == 1:
            promedioAnualluvias = promedioAnualluvias()
            pass

    return lluvia, promedioAnualluvias


lluvias, promedioAnualluvias = main()
