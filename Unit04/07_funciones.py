'''Calcular nuevo salario de trabajar si tuvo un aumento de "x"%'''


salario = int(input('Ingrese salario: '))
aumento = int(input('Ingrese "%" de aumento: '))


def calcularNewSalary(salario, aumento):
    return (salario*aumento) // 100


aumentoNuevo = calcularNewSalary(salario, aumento)

sueldoBruto = aumentoNuevo + salario


# Scrip principal

print('Su nuevo sueldo es: ', sueldoBruto)
