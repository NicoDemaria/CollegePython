# 2. Último y Primero
# Desarrollar un programa que permita cargar por teclado un vector de n elementos y luego:

# Informe cuántas veces se repite en el vector el último número ingresado
# Genere un nuevo vector, conteniendo sólo los elementos menores al primer valor ingresado.


def validartamanio():
    n = int(input('Ingrese el tamanio de el vector: '))
    while n <= 0:
        n = int(input('El tamaño debe ser positivo. Ingrese otro: '))
    return n


def cargaDatos(n):
    vector = []
    for i in range(n):
        dato = int(input('Ingrese el elemento: '))
        vector.append(dato)
    return vector


def contadorUltimo(vector):
    repecionesUlt = 0
    for elemento in vector:
        if elemento == vector[-1]:
            repecionesUlt += 1
    return repecionesUlt - 1


def contadorPrimer(vector):
    menores = []
    primerValor = vector[0]
    for elemento in vector:
        if elemento < primerValor:
            menores.append(elemento)
    return menores


def main():
    tamanio = validartamanio()
    vector = cargaDatos(tamanio)
    cantidadUltimo = contadorUltimo(vector)
    menores = contadorPrimer(vector)
    print('Se repite el ultimo numero ingresado: ',
          cantidadUltimo,  'cantida de veces')
    print('Los elementos menores al primer valor ingresado son los siguientes: ', menores)


main()
