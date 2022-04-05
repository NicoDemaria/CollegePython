# 11. Galería de arte
# Una galería de arte desea preparar un catálogo de sus cuadros más famosos.

# Se realiza una prueba con tres cuadros y por cada uno se ingresa el año en que fue creado. El programa deberá:

# Verificar si todos los cuadros son anteriores al siglo XX(El siglo XX es el siglo pasado. Se inició en el año 1901 y terminó en el año 2000).
# Determinar si alguna de las obras fue creada en un año que se ingresa por teclado.
# Informar la diferencia en años entre la obra más nueva y la más antigua.

cuadro1 = int(input('Ingrese el ano de el cuadro1: '))
cuadro2 = int(input('Ingrese el ano de el cuadro2:'))
cuadro3 = int(input('Ingrese el ano de el cuadro3: '))

if cuadro1 < 1901:
    print('El primer cuadro es anterior a 1901 ')
else:
    print('El primer cuadro se creo dps de XX')
if cuadro2 < 1901:
    print('El segundo cuadro es anterior a 1901 ')
else:
    print('El segundo cuadro se creo dps de XX')
if cuadro3 < 1901:
    print('El tercer cuadro es anterior a 1901 ')
else:
    print('El tercer cuadro se creo dps de XX')


if cuadro1 == cuadro2:
    print('El cuadro 1 se creo en el mismo ano que el cuadro 2')
elif cuadro1 == cuadro3:
    print('El cuadro 1 se creo en el mismo ano que el cuadro 3')
else:
    print('Los anos de los cuadros son diferentes')

if cuadro2 == cuadro1:
    print('El cuadro 2 se creo en el mismo ano que el cuadro 1')
elif cuadro2 == cuadro3:
    print('El cuadro 2 se creo en el mismo ano que el cuadro 3')
else:
    print('Los anos de los cuadros son diferentes')

if cuadro3 == cuadro1:
    print('El cuadro 3 se creo en el mismo ano que el cuadro 1')
elif cuadro3 == cuadro2:
    print('El cuadro 3 se creo en el mismo ano que el cuadro 2')
else:
    print('El ano de el cuadro 3 es  diferentes')






