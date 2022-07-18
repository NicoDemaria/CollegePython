'''
Calculador el iva de una compra siendo el iva 19%
'''


precio = float(input('Ingrese el precio de la compra: '))


def iva(precio):
    return precio * 0.19


ivaProducto = iva(precio)
print('El precio de su su producto es: ', precio)
print('El iva de su producto es: ', ivaProducto)
print('El precio total de su producto es: ', precio + ivaProducto)
