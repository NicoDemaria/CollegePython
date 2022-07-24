'''10. Portal de empleo
Un conocido portal de empleo requiere un programa para validar las búsquedas que se cargan en su página. Por cada búsqueda se requiere:

CUIT: validar que sea un texto compuesto por 13 números separados por guiones de la siguiente manera: 00-00000000-0
Descripción de la búsqueda: un texto donde cada palabra se separa con un espacio y termina con punto. Debe tener un máximo de 60 caracteres y un mínimo de 3 palabras. Ninguna palabra debe contener dos mayúsculas seguidas.
Salario ofrecido: controlar que sea un valor mayor a 0
Si todos los datos son válidos, mostrar el aviso completo. En caso contrario, informar que no es posible mostrarlo.

Para terminar, consultar al usuario si desea cargar otro aviso o salir del programa.
'''


def validar_cuit(cuit):
    valido = False
    digitosNumericos = 0
    if len(cuit) == 13:
        if cuit[2] == '-' and cuit[11] == '-':
            for car in cuit:
                if car in '0123456789':
                    digitosNumericos += 1

            if digitosNumericos == 11:
                valido = True
    return valido


def validarDesc(descripcion):
    valido = False
    palabras = 0
    mayusSeguidas = False
    anterior = ''
    if len(descripcion) <= 60:
        for car in descripcion:
            if car == ' ' or car == '.':
                palabras += 1
            else:
                if car >= 'A' and car <= 'Z' and anterior >= 'A' and anterior <= 'Z':
                    mayusSeguidas = True

            anterior = car
        if palabras <= 3:
            if mayusSeguidas == False:
                valido = True
    return valido


def main():
    # Datos de entrada
    cuit = input('Ingrese el CUIT: ')
    descripcion = input('Ingrese la descripción de la búsqueda: ')
    salario = input('Ingrese el salario ofrecido: ')

    # Procesos

    cuitValido = validar_cuit(cuit)
    descValido = validarDesc(descripcion)
    SalarioValido = True

    # Output
    print('='*80)
    if cuitValido and descValido and SalarioValido:
        print('Todos los datos son validos')
        print('Empleado:', cuit)
        print('Desc:', descripcion)
        print('Salario:', salario)

    else:
        print('Alguno de los datos no son validos, no se puede mostrar ')

    print('='*80)


#
main()
