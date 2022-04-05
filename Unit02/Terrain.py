# 10. Terreno
# Se ingresan las medidas de frente y fondo de un terreno.

# Determinar si es cuadrado o rectangular y calcular su superficie.

frente = float(input('Enter la medida frente de el terreno: '))
fondo = float(input('Enter la medida fondo de el terreno: '))


if frente == fondo:
    print('El terreno es cuadrado ya que son miden lo mismo en alto y ancho', frente, fondo)
else:
    print('El terreno es rectangular ya que sus lados no miden lo mismo', frente, fondo)
