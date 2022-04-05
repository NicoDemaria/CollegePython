# 9. Edad mínima
# Ingresar por teclado las edades de 3 participantes de un concurso.

# Informar si todos cumplen con la edad mínima establecida para el mismo, también ingresada por teclado.

minimumAge = int(input('Enter the minimum age: '))

a1 = int(input('Please enter the age of the first participant: '))
a2 = int(input('Please enter the age of the second participant: '))
a3 = int(input('Please enter the age of the second participant: '))

if a1 > minimumAge:
    print('The first contestant can pass.')
else:
    print("the first contestant can't pass.")
if a2 > minimumAge:
    print('The second contestant can pass.')
else:
    print("the second contestant can't pass.")
if a3 > minimumAge:
    print('The third contestant can pass.')
else:
    print("the third contestant can't pass.")
