# Desarrollar un programa en Python que permita cargar por teclado un texto completo (analizar dos opciones: una es cargar todo el texto en una variable de tipo cadena de caracteres y recorrerla con un for iterador; y la otra es cargar cada caracter uno por uno a través de un while). Siempre se supone que el usuario cargará un punto para indicar el final del texto, y que cada palabra de ese texto está separada de las demás por un espacio en blanco. El programa debe:

# a) Determinar cuántas palabras tenían más de 4 letras.

# b) Determinar cuántas palabras tenían al menos una vez la letra "x" o la letra "y".

# c) Determinar el promedio de letras por palabra en todo el texto.

# d) Determinar cuántas palabras contuvieron sólo una vez la expresión "mo".

# ********************************************************************************
# Ejemplo: 'el mono momoxy toca el xilofon.'
# ********************************************************************************
# Palabras con más de 4 letras: 2
# Palabras tenían al menos una vez la letra "x" o la letra "y": 2
# El promedio de letras por palabra en todo el texto es: 4.17
# Determinar cuántas palabras contuvieron sólo una vez la expresión "mo": 1


cadenaCaracteres = str(input('Ingrese un texto: '))
contadorCadenas = 0
for i in cadenaCaracteres:
    if i.__len__\
