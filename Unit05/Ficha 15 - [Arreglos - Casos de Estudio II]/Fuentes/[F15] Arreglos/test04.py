__author__ = 'Cátedra de AED'


def validate(inf):
    k = inf
    while k <= inf:
        k = int(input('Ingrese valor de k (mayor a ' + str(inf) + ' por favor): '))
        if k <= inf:
            print('Error: se pidio mayor a', inf, '... cargue de nuevo...')

    return k


def is_ok(cad, ABC):
    if cad is None:
        return False

    if cad == '':
        return False

    for i in range(len(cad)):
        # si cad[i] no es blanco y no está en el alfabeto, retornar False...
        if cad[i] != ' ' and ABC.find(cad[i]) == -1:
            return False

    return True


def code_cesar(mens, ABC, k):
    if not is_ok(mens, ABC):
        return None

    na = len(ABC)
    b = []
    for i in range(len(mens)):
        # si el caracter original es blanco, dejar ese blanco...
        if mens[i] == ' ':
            b.append(' ')

        # si el caracter original no es blanco, reemplazarlo...
        else:
            # indice del caracter mens[i] en el alfabeto...
            im= ABC.find(mens[i])

            # indice del caracter de reemplazo en el alfabeto...
            ir = (im + k) % na

            # efecturar el reemplazo en el arreglo de salida b...
            b.append(ABC[ir])

    # convertir el arreglo b a cadena de caracteres y retornar...
    encr = ''.join(b)
    return encr


def decode_cesar(encr, ABC, k):
    if not is_ok(encr, ABC):
        return None

    na = len(ABC)
    b = []
    for i in range(len(encr)):
        # si el caracter encriptado es blanco, dejar ese blanco...
        if encr[i] == ' ':
            b.append(' ')

        # si el caracter encriptado no es blanco, reemplazarlo...
        else:
            # indice del caracter encr[i] en el alfabeto...
            ie = ABC.find(encr[i])

            # indice del caracter original en el alfabeto...
            io = (ie - k + na) % na
            b.append(ABC[io])

    # convertir el arreglo b a cadena de caracteres y retornar...
    mens = ''.join(b)
    return mens


def code_transposition(mens, ABC, TRANS):
    if not is_ok(mens, ABC):
        return None

    b = []
    for i in range(len(mens)):
        # si el caracter original es blanco, dejar ese blanco...
        if mens[i] == ' ':
            b.append(' ')

        else:
            # si el caracter original no es blanco, reemplazarlo...
            im = ABC.find(mens[i])
            b.append(TRANS[im])

    # convertir el arreglo b a cadena de caracteres y retornar...
    encr = ''.join(b)
    return encr


def decode_transposition(encr, ABC, TRANS):
    if not is_ok(encr, ABC):
        return None

    b = []
    for i in range(len(encr)):
        # si el caracter encriptado es blanco, dejar ese blanco...
        if encr[i] == ' ':
            b.append(' ')

        # si el caracter encriptado no es blanco, reemplazarlo...
        else:
            # si el caracter encriptado no es blanco, reemplazarlo...
            ie = TRANS.find(encr[i])
            b.append(ABC[ie])

    # convertir el arreglo b a cadena de caracteres y retornar...
    mens = ''.join(b)
    return mens


def test():
    # el alfabeto general...
    ALFABETO = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

    # Cifrado de César...
    # cargar el mensaje a encriptar (sin validación)...
    mensaje = input('Mensaje a encriptar (sólo mayúsculas y blancos...): ')
    print()

    print('Encriptación de César...')

    # cargar el valor del desplazamiento k...
    k = validate(1)

    # encriptar el mensaje con encriptación de César...
    encriptado = code_cesar(mensaje, ALFABETO, k)

    # desencriptar el mensaje encriptado (para comprobación)...
    desencriptado = decode_cesar(encriptado, ALFABETO, k)

    # si no hubo problemas, mostrar mensaje en claro y mensaje encriptado...
    if encriptado is not None:
        print('Mensaje original (tal como se cargó por teclado):', mensaje)
        print('Mensaje encriptado con clave k=', k, ': ', encriptado, sep='')
        print('Mensaje desencriptado (a partir del encriptado):', desencriptado)
    else:
        print('Error: posiblemente está mal el formato del mensaje original...')

    # Cifrado de Transposición...
    print()
    print('Encriptación de Transposición...')

    # una tabla de transposición para el alfabeto dado...
    TRANSPOSICION = "RISQPANOWXUMDHZTFGBLEYKCJVÑ"

    # encriptar el mensaje con encriptación de Transposición...
    encriptado = code_transposition(mensaje, ALFABETO, TRANSPOSICION)

    # desencriptar el mensaje encriptado (para comprobación)...
    desencriptado = decode_transposition(encriptado, ALFABETO, TRANSPOSICION)

    # si no hubo problemas, mostrar mensaje en claro y mensaje encriptado...
    if encriptado is not None:
        print('Mensaje original (tal como se cargó por teclado):', mensaje)
        print('Mensaje encriptado (tabla usada: ', TRANSPOSICION, '): ', encriptado, sep='')
        print('Mensaje desencriptado (a partir del encriptado):', desencriptado)
    else:
        print('Error: posiblemente está mal el formato del mensaje original...')


# script principal...
if __name__ == '__main__':
    test()
