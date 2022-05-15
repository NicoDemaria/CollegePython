import random



random.seed(10)
n = 10000
numerosNegativos = 0
sumador0600 = 0
numeros200 = 0
divisibles4 = 0
men = 0
truncador = 0
negativosPares = 0
for i in range(n):
    num = random.randint(-500, 1000)

    #1

    if num < 0:
        numerosNegativos += 1

    if num >= 0 and num <= 600:
        sumador0600 += num

    if num >= 200:
        if num % 10 == 2:
            numeros200 += 1
        else:
            if num % 10 == 3:
                numeros200 += 1

    #2

    if num < 0 and num % 4 == 0:
        divisibles4 += 1
        promedio4 = n//divisibles4

    #3

    if num > 100 and num % 2 != 0:
        if i == 0:
            men = num
        elif num < men:
            men = num

    #4

    if num % 2 == 0 and num < 0:
        truncador +=1
        negativosPares += 1
porcentaje = (negativosPares * truncador) // 100


print('Consigna 1:', numerosNegativos, sumador0600, numeros200)


print('El promedio es:',promedio4)

print('El menor es: ', men)

print('El porcentaje es:', porcentaje )