__author__ = 'Cátedra de AED'


def validate(inf):
    n = inf
    while n <= inf:
        n = int(input('Ingrese cantidad de elementos (mayor a ' + str(inf) + ' por favor): '))
        if n <= inf:
            print('Error: se pidio mayor a', inf, '... cargue de nuevo...')

    return n


def read(nombres, edades, sueldos):
    n = len(nombres)
    for i in range(n):
        nombres[i] = input('Nombre[' + str(i) + ']: ')
        edades[i] = int(input('Edad: '))
        sueldos[i] = int(input('Sueldo: '))
        print()


def sort(nombres, edades, sueldos):
    n = len(nombres)
    for i in range(n-1):
        for j in range(i+1, n):
            if nombres[i] > nombres[j]:
                nombres[i], nombres[j] = nombres[j], nombres[i]
                edades[i], edades[j] = edades[j], edades[i]
                sueldos[i], sueldos[j] = sueldos[j], sueldos[i]


def display(nombres, edades, sueldos):
    n = len(nombres)
    print('Personas mayores de 18 que ganan menos de 10000 pesos:')
    for i in range(n):
        if edades[i] > 18 and sueldos[i] < 10000:
            print('Nombre:', nombres[i], '- Edad:', edades[i], '- Sueldo:', sueldos[i])


def test():
    # cargar cantidad de personas...
    n = validate(0)

    # crear los tres arreglos de n elementos...
    nombres = n * [' ']
    edades = n * [0]
    sueldos = n * [0]

    # cargar los tres arreglos por teclado...
    print('\nCargue los datos de las personas:')
    read(nombres, edades, sueldos)

    # ordenar alfabéticamente el sistema...
    sort(nombres, edades, sueldos)

    # avisar por pantalla el resultado de la búsqueda...
    display(nombres, edades, sueldos)


# script principal...
if __name__ == '__main__':
    test()