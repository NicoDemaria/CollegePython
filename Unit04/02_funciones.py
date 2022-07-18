'''Programa que tome 3 nota de un estudiante y diga la nota final del curso
La primera nota valen y segunda nota valen un 30% y la tercera nota valen un 40%
'''


def calcularNota(nota1, nota2, nota3):
    return (nota1 * 0.3) + (nota2 * 0.3) + (nota3 * 0.4)


nota1 = int(input('Ingrese la primera nota: '))
nota2 = int(input('Ingrese la segunda nota: '))
nota3 = int(input('Ingrese la tercera nota: '))

notaFinal = calcularNota(nota1, nota2, nota3)
print('La nota final es: ', notaFinal)
