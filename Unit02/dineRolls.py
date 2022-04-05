# 8. Lanzamiento de dados
# Simular un juego en el que se lanzan dos dados.

#  Si ambos dados son iguales o la suma entre ellos es impar, gana el usuario. En caso contrario, gana la máquina.

import random
print('Si ambos dados son iguales o la suma entre ellos es impar, gana el usuario. En caso contrario, gana la máquina')

print('A continuacion se lanzaran los dados, por favor espere...')
dados1 = random.randint(1, 6)
dados2 = random.randint(1, 6)

print('Dado 1 : ', dados1)
print('Dado 2 : ', dados2)

sumDados = dados1 + dados2

if dados1 == dados2:
    print('Ambos dados son iguales, gana el usuario')
elif sumDados % 2 == 0:
    print('La suma de los dados es par, gana la máquina')
else:
    print('La suma de los dados en impar, gana el usuario')
