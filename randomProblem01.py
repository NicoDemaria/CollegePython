import random

print('COMPARATION BETWEEN TWO RANDOMS NUMBERS GIVEN')
x1 = random.randrange(1, 11)
x2 = random.randrange(1, 11)
print('n1 ===> ', x1, ' n2 ===> ', x2)


if x1 > x2:
    print('The first number is bigger than the second')
elif x1 == x2:
    print('both numbers are equal')
else:
    print('The second number is bigger than the first')


print('C:')
