# Problema 10.) Cargar por teclado tres números enteros que se supone representan las edades de tres personas. Determinar si alguno de los valores cargados era negativo, en cuyo caso informe en pantalla con un mensaje tal como: Alguna es incorrecta: negativa. Si todos los valores eran positivos o cero, informe que todas eran correctas.


a1 = int(input('Please, enter the first age: '))
a2 = int(input('Please, enter the second age: '))
a3 = int(input('Please, enter the third age: '))


if a1 >= 0 and a2 >= 0 and a3 >= 0 and a1 <= 100 and a2 <= 100 and a3 <= 100:
    print('All ages are correct')
else:
    print('One or more ages are incorrect')
