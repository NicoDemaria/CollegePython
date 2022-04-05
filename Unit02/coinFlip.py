# 7. Tirada de moneda
# Programar una tirada de una moneda (opciones: cara o cruz) aleatoriamente. Permitir que un jugador apueste a cara o cruz y luego informar si acertó o no con su apuesta.

import random

print('welecome to the coin flip game, if your bet is correct you win, if not you lose, number one is heads, number two is tails')

coinEntry = int(input(
    'Please enter heads or tails(0 for heads and 1 is for tails): '))


if coinEntry == 0:
    coinEntry = 'heads'
elif coinEntry == 1:
    coinEntry = 'tails'
else:
    print('You have entered an invalid entry, please try again')
    exit()


print('The coin is flipping...')
print('...')
print('The coin is ==>', coinEntry)
