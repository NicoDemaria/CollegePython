# comprobar el mayor de los numeros

n1 = (input('please, enter a number: '))
n2 = (input('please, enter a number: '))


def mayor(n1, n2):
    if n1 > n2:
        print('The first number is higher than n2', n1)
    elif n1 == n2:
        print('The number are equal')
    else:
        print('The second number is higher than n1:', n2)


print(mayor(n1, n2))
