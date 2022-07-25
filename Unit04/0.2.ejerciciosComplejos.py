'''11. Inicio y fin con vocal
Se solicita crear un programa que permita ingresar un texto, las palabras se encontrarán separadas únicamente por espacios en blanco y el mismo debe finalizar con un punto. En base a ese texto determinar:

a) La cantidad de palabras que comienzan y terminan en vocal

b) La cantidad de palabras que comienzan con la misma letra que terminó la palabra anterior

c) El porcentaje que representa el punto a) sobre el total de palabras del texto'''


def verificartexto(texto):
    palabra = 0
    contadorVocal = 0
    for car in texto:
        if car == ' ' or car == '.':
            print
        else:
            if car in 'AEIOUaeiou':
                print


def main():
    texto = input('Ingrese un texto')

    vocalreturn = verificartexto(texto)


main()
