import aed.validadores as validadores
import aed.menus as menus

__author__ = 'philip'


def mostrar_menu():
    print('Menú de opciones')
    print('1 - Validar Entero')
    print('2 - Validar Flotante')
    print('3 - Convertir Entero')
    print('4 - Convertir Flotante')
    print('0 - Salir')


def validacion_entero():
    print('Opción Validar un Número entero desde la cadena que se carga por teclado')

    entrada = input('Ingrese un nro: ')
    while not validadores.validar_cadena_entero(entrada):
        print('Error: solo cargar un número entero...')
        entrada = input('Ingrese un nro: ')
    nro = int(entrada)
    print(f'Número entero cargado: {nro}')


def validacion_flotante():
    print('Opción Validar un Número flotante desde la cadena que se carga por teclado')
    entrada = input('Ingrese un nro: ')
    while not validadores.validar_cadena_decimal(entrada):
        print('Error: solo cargar un número entero...')
        entrada = input('Ingrese un nro: ')
    nro = float(entrada)
    print(f'Número entero cargado: {nro}')


def conversion_entero():
    print('Opción Convertir una cadena en un numero entero (emular la función int() sin usarla)')
    print('Hagan uds.')


def conversion_flotante():
    print('Opción Convertir una cadena en un numero flotante (emular la función float() sin usarla)')
    print('Hagan uds.')


def procesar(opc):
    if opc == 1:
        validacion_entero()
    elif opc == 2:
        validacion_flotante()
    elif opc == 3:
        conversion_entero()
    elif opc == 4:
        conversion_flotante()
    else:
        print('Chau chau chaaaauuuuuuuuu!!!!')


def inicio():
    opciones = ('Validar Entero',
               'Validar Flotante',
               'Convertir Entero',
               'Convertir Flotante')
    opc = None
    while(opc != 0):
        # Mostrar el menú con la versión estática
        # mostrar_menu()
        # Ahora con la versión dinámica
        # menus.mostrar_menu(opciones,'Menú de Opciones')

        # Leo la opcion elegida
        # opc = validadores.leer_entero_en_rango(0, 4, 'Ingrese la opción: ')

        # Ahora con la versión automática
        # opc = menus.ingresar_opcion_menu(opciones, 'Ociones ->')

        # Ahora con la versión de ventanitas
        opc = menus.menu_opciones_gui(opciones, 'Elija una opción', 'Menú de Opciones')

        # Proceso la opción elegida
        procesar(opc)

        print('\n\n')


if __name__ == "__main__":
    inicio()
