# Escriba un programa que pida la anchura y altura de un rectángulo y lo dibuje con caracteres producto (*):


ancho = int(input("Ingrese el ancho del rectángulo: "))
altura = int(input("Ingrese la altura del rectángulo: "))


def dibujar_rectangulo(ancho, altura):
    for i in range(altura):
        for j in range(ancho):
            print("*", end="")
        print()
