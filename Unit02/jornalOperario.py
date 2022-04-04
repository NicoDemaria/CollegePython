# Se necesita desarrollar un programa para el área de recursos humanos de una empresa que permita informar el jornal de un determinado operario. Usted deberá cargar por teclado el código de turno que el operario trabajó ese día(1 - representa Diurno y 2 - representa Nocturno) y la cantidad de horas trabajadas.

# La política de trabajo en la empresa es que los operarios de la misma pueden trabajar en el turno diurno o nocturno. Si un operario trabaja en el turno nocturno el pago es 40.60 pesos la hora, si lo hace en el turno diurno cobra 35.50 pesos la hora.

codeWork = int(input('Enter the code of the work(1 => day, 2 => night): '))
hoursWork = float(input('Enter the hours worked: '))

if codeWork == 1:
    hoursWork = hoursWork * 35.50
elif codeWork == 2:
    hoursWork = hoursWork * 40.60

print('The salary is: ', hoursWork)
