__author__ = 'philip'

# Importar el módulo para tener acceso a todas sus funciones a partir de su nombre
import aed.validadores as validadores
try:
	import PySimpleGUI as sg
	sg_is_present = True
except ImportError:
	sg_is_present = False

# Importar las funciones del módulo como si estuvieran programadas localmente
from aed.validadores import leer_entero_en_rango



def ingresar_opcion_menu(tupla_opciones, titulo='Opciones'):
	print()
	print('=' * (len(titulo) + 4))
	print(f'= {titulo} =')
	print('=' * (len(titulo) + 4))
	contador = 1
	for opcion in tupla_opciones:
		print(f'{contador} - {opcion}')
		contador += 1
	print('0 - Salir')
	opcion = validadores.leer_entero_en_rango(0, len(tupla_opciones), 'Seleccione una opción: ', 'No sea sonso y lea el menú...')
	return opcion


def mostrar_menu(opciones, titulo='Opciones...'):
	print('*' * (len(titulo) + 4))
	print('*', titulo, '*')
	print('*' * (len(titulo) + 4))
	print()
	nro_opcion = 1
	for opcion in opciones:
		print(f'{nro_opcion} - {opcion}')
		nro_opcion += 1
	print('0 - Salir')


def menu_opciones_gui(opciones, titulo='Menú de Opciones', cabecera='Menú de Opciones'):
	if sg_is_present:
		sg.theme('Reds')

		controles = []
		controles.append([sg.Text(titulo, font='Any 20')])
		numero_opcion = 0
		for opc in opciones:
			numero_opcion += 1
			controles.append([sg.Button(opc, key=f'{numero_opcion}',expand_x=True,highlight_colors=('Black','Orange'),mouseover_colors=('Black','Orange'))])
		controles.append([sg.Button('Salir', key=f'0', expand_x=True)])
		controles.append([sg.Text(size=(50, None))])

		layout = controles

		window = sg.Window(cabecera, controles, keep_on_top=True, resizable=False, text_justification='Left')

		event, values = window.read()
		window.close()

		if event is None:
			event = '0'
		return int(event)
	else:
		return ingresar_opcion_menu(opciones, titulo)


def prueba():
	opcs = ('Suma', \
		    'Producto', \
		    'Factorial')

	mostrar_menu(opcs, 'Menú de Opciones')
	print('\nCon la carga...')
	opc = ingresar_opcion_menu(opcs, 'Menú con carga de opción')
	print(opc)
	opc = menu_opciones_gui(opcs, 'Menú con botones', 'Menú de Opciones')
	print(opc)

if __name__ == '__main__':
	print(f'Nombre módulo menus: {__name__}')
	prueba()
