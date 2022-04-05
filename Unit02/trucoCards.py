# Desarrollar un programa que genere al azar tres cartas simulando una mano de truco. A continuación deberá:
#
# Informar si entre las cartas se encuentra el as de espadas
# Verificar si las tres cartas son del mismo palo. Si es así, mostrar la suma de las dos mayores. En caso contrario, informarlo.

import random
manoTruco = random.randint(1,1)
manoTruco2 = random.randint(1,12)
manoTruco3 = random.randint(1,12)

palos = ['Espada','Basto','Oro','Copa']
manoPalo1  = random.choices(palos)
manoPalo2  = random.choices(palos)
manoPalo3  = random.choices(palos)


mano1 = (manoTruco,manoPalo1)
mano2 = (manoTruco2,manoPalo2)
mano3 = (manoTruco3,manoPalo3)
print(mano1,mano2,mano3)

if mano1 == (1, ['Espada']) or mano2 == (1, ['Espada']) or mano3 == (1, ['Espada']):
    print('Te toco el macho')
else:
    print('No te toco el macho')



maxCard = (max(manoTruco,manoTruco2,manoPalo3))

if manoPalo1 == manoPalo2 == manoPalo3:
    print(maxCard)




