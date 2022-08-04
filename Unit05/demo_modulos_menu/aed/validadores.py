"""
    Módulo dedicado a funciones de validación de entrada.

    En esté módulo encontraremos todas las funciones que vamos creando a lo largo del año para validar entrada de datos
    entre ellas tenemos funciones para validar enteros positivos, enteros en un rango, funciones para validar si una
    cadena puede ser convertida a entero, o a flotante, etc.

    Lista de funciones incluidas:
    :leer_entero_en_rango(límite_inferior, límite_superior, mensaje, mensaje_error): Permite leer un número entero
        desde el teclado validando que esté en el rango indicado.
    :leer_entero_positivo(): Permite leer un número entero desde el teclado validando que sea mayor a cero.
"""
__author__ = 'philip'

from aed.caracteres import *


def leer_entero_en_rango(limite_inferior, limite_superior,
                         mensaje='Ingrese un número entero: ',
                         mensaje_error='Error el número debe estar en el rango permitido'):
    """
        Esta función permite leer un número entero validando que se encuentre dentro del rango indicado por los parámetros.

    Documentación detallada del funcionamiento de la función
    :param limite_inferior: Límite inferior del rango permitido
    :param limite_superior: Límite superior del rango permitido
    :param mensaje: Mensaje mostrado al usuario en el input
    :param mensaje_error: Mensaje mostrado al usuario en caso de error.
    :return: el numero entero válido
    """
    # Inicio del cuerpo
    entrada = input(mensaje)
    while not validar_cadena_entero(entrada):
        print('Error: debe ingresar un número entero...')
        entrada = input(mensaje)
    var = int(entrada)
    # Condición de validación "tiene que dar True cuando el valor cargado está mal!"
    while var < limite_inferior or var > limite_superior:
        print(mensaje_error)
        entrada = input(mensaje)
        while not validar_cadena_entero(entrada):
            print('Error: debe ingresar un número entero...')
            entrada = input(mensaje)
        var = int(entrada)
    # Qué me falta? devolver
    return var


def leer_entero_positivo(mensaje):
    """
        Esta función permite leer y validar un entero mayor a cero
    :param mensaje: Mensaje a mostrar al usuario
    :return: número entero validado.
    """
    entrada = input(mensaje)
    while not validar_cadena_entero(entrada):
        print('Error: debe ingresar un número entero...')
        entrada = input(mensaje)
    x = int(entrada)
    while x <= 0:
        print('El valor deber ser positivo no sea sonso....')
        entrada = input(mensaje)
        while not validar_cadena_entero(entrada):
            print('Error: debe ingresar un número entero...')
            entrada = input(mensaje)
        x = int(entrada)
    return x


def validar_cadena_entero(entrada):
    resultado = True

    if entrada is None or len(entrada) == 0:
        resultado = False
    else:
        digitos = 0
        posicion = 0
        for car in entrada:
            posicion += 1
            if posicion == 1:
                if not es_digito(car) and not es_signo(car):
                    resultado = False
                    break
            elif not es_digito(car):
                resultado = False
                break
            if es_digito(car):
                    digitos += 1
        else:
            resultado = digitos > 0
        return resultado


def validar_cadena_decimal(entrada):
    resultado = True
    
    if entrada is None or len(entrada) == 0:
        resultado = False
    else:
        digitos = 0
        puntos = 0
        posicion = 0
        for car in entrada:
            posicion += 1
            if posicion == 1:
                if not es_digito(car) and not es_signo(car) and not car == '.':
                    resultado = False
                    break
            else:
                if not es_digito(car):
                    if car == '.':
                        puntos += 1
                    else:
                        resultado = False
                        break
            if es_digito(car):
                digitos += 1
        else:
            resultado = digitos > 0 and puntos <= 1
            
    return resultado


def prueba():
    # print('Modulo validadores valor de __name__', __name__)
    # print('Leer entero entre 1 y 10')
    # Llamada a la función con argumentos posicionales
    n = leer_entero_en_rango(1, 10, 'Ingrese la nota del alumno: '
                             , 'La nota es un número entero entre 1 y 10')
    # Llamada con argumentos o parámetros con nombre
    # n = leer_entero_en_rango(mensaje='Ingrese la nota del alumno: '
    #                          , mensaje_error='La nota es un número entero entre 1 y 10', limite_inferior=1, limite_superior=10)
    # Llamada a la función con valores por defecto
    # n = leer_entero_en_rango(1, 10)
    # print('La nota ingresada es:', n)
    print('Prueba números enteros...')
    print('0 ==> ', validar_cadena_entero('0'))
    print('1234 ==> ', validar_cadena_entero('1234'))
    print('1 234 ==> ', validar_cadena_entero('1 234'))
    print('+1234 ==> ', validar_cadena_entero('+1234'))
    print('-1234 ==> ', validar_cadena_entero('-1234'))
    print('12.34 ==> ', validar_cadena_entero('12.34'))
    print('A1234 ==> ', validar_cadena_entero('A1234'))
    print('12A34 ==> ', validar_cadena_entero('12A34'))
    print("'' ==> ", validar_cadena_entero(''))
    print("input('Ingrese un número entero: ') ==> ", validar_cadena_entero(input('Ingrese un número entero: ')))
    print('Prueba números flotantes')
    print('0 ==> ', validar_cadena_decimal('0'))
    print('1234 ==> ', validar_cadena_decimal('1234'))
    print('1.234,25 ==> ',  validar_cadena_decimal('1.234,25'))
    print('1.234.567,89 ==> ',  validar_cadena_decimal('1.234.567,89'))
    print('1.234.567 ==> ',  validar_cadena_decimal('1.234.567'))
    print('.1234 ==> ',  validar_cadena_decimal('.1234'))
    print('1234. ==> ',  validar_cadena_decimal('1234.'))
    print('1 234 ==> ', validar_cadena_decimal('1 234'))
    print('+12.34 ==> ', validar_cadena_decimal('+12.34'))
    print('-123.4 ==> ', validar_cadena_decimal('-123.4'))
    print('-.1234 ==> ', validar_cadena_decimal('-.1234'))
    print('.-1234 ==> ', validar_cadena_decimal('.-1234'))
    print('12.34 ==> ', validar_cadena_decimal('12.34'))
    print('A12.34 ==> ', validar_cadena_decimal('A12.34'))
    print('12.A34 ==> ', validar_cadena_decimal('12.A34'))
    print("'' ==> ", validar_cadena_entero(''))
    print("input('Ingrese un número flotante: ') ==> ", validar_cadena_decimal(input('Ingrese un número flotante: ')))


# Script principal
if __name__ == '__main__':
    print(f'Nombre módulo validadores: {__name__}')
    # print(f'Documentación: \n{__doc__}')
    prueba()
