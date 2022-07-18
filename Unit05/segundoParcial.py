def es_vocal(caracter):
    return caracter in 'aeiouAEIOUáéíóú'


def principal():

    texto = input(str('Ingrese un texto.'))
    texto = texto.lower()
    contadorPalabras = 0
    contadorVocales = 0

    contadorLetras = 0
    TieneQ = False
    NocontieneZQ = False
    for letra in texto:

        if letra != ' ' and letra != '.':
            contadorLetras += 1
            if es_vocal(letra):
                contadorVocales += 1

        if letra == 'q' or letra == 'Q':
            TieneQ = True
