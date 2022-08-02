'''Desarrollar un programa que permita cargar tres arreglos con n nombres de personas, sus edades y los sueldos que ganan. Luego de realizar la carga de todos los datos, mostrar los nombres de las personas mayores de 18 años que ganan menos de 10000 pesos, pero de
forma que el listado salga ordenado en forma alfabética.'''


def main():
    n = int(input('Ingrese la cantidad de modulos de el arreglo:'))
    nombre = n * [0]
    edad = n * [0]
    sueldo = n * [0]
    for i in range(n):
        nombre[i] = input('Ingrese el nombre de la la persona:')
        edad[i] = input('Ingrese la edad  de la la persona:')
        sueldo[i] = input('Ingrese el sueldo de la persona de la la persona:')
    return nombre, edad, sueldo


nombre, edad, sueldo = main()
print(nombre)
print(edad, 'Years')
print(sueldo, '$')
