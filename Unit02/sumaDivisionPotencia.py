# Se necesita desarrollar un programa que permita calcular la suma de tres números. Si el resultado es mayor a 10 dividir por 2 (mostrar su resultado sin decimales), en caso contrario elevar el resultado al cubo.

n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))
n3 = int(input('Enter the third number: '))

numSum = n1 + n2 + n3

if numSum > 10:
    print('The sum of the numbers is: ', numSum,
          ' and the result is: ', numSum // 2)
else:
    print('The sum of the numbers is: ', numSum,
          ' and the result is: ', numSum ** 3)
