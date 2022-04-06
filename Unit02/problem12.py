# Problema 12.) Una compañía de alquiler de automóviles necesita un programa que calcule lo que se debe cobrar a cada cliente, teniendo en cuenta el kilometraje recorrido por el cliente al devolver el automóvil:
# i. Si el cliente no superó los 300 km recorridos se deberá cobrar $500.
# ii. Para recorridos desde más de 300 km y hasta no más de 1000 km se le cobrará $500 más el kilometraje excedente a los 300, a razón de $3 por kilómetro.
# iii. Para recorridos mayores a 1000 km se le cobrará $500 más el kilometraje excedente a los 300, a razón de $1.5 por kilómetro.


recorridoClient = int(input('Ingrese los KM recorridos: '))

if recorridoClient <= 300:
    print('Se debera cobrar 500$.')
elif recorridoClient >= 300 and recorridoClient <= 1000:
    multa1 = (recorridoClient - 300) * 3
    print('La nueva tarifa debido al exceso es: ', multa1 + 500)
else:
    if recorridoClient >= 1000:
        multa2 = (recorridoClient - 300 ) *1.5
        print('se le cobrará $500 más el kilometraje excedente a los 300, a razón de $1.5 por kilómetro.', multa2 + 500)

print('Fin de el programa pague por favor!.')