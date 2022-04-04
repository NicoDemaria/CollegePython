# Se solicita realizar un programa que permita ingresar tres temperaturas correspondientes a diferentes momentos de un día y determinar:

# Cual es el promedio de las temperaturas.
# Si existe alguna temperatura que sea mayor al promedio.

t1 = float(input('Please, enter the first temperature: '))
t2 = float(input('Please, enter the second temperature: '))
t3 = float(input('Please, enter the third temperature: '))

temperatureSum = t1 + t2 + t3
print('The sum of the temperatures is: ', temperatureSum, '\n ')
temperatureAverage = temperatureSum / 3
print('The average of the temperatures is: ', temperatureAverage, '\n ')

if t1 > temperatureAverage:
    print('The first temperature is greater than the average. ==> ', t3, '\n ')
elif t2 > temperatureAverage:
    print('The second temperature is greater than the average. ==> ', t2, '\n ')
elif t3 > temperatureAverage:
    print('The third temperature is greater than the average. ==> ', t3), '\n '
else:
    print('There is no temperature greater than the average.')
