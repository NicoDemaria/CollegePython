import random

x = random.randrange(1, 11)
print('Numero aleatorio de el intervalo [1,10] ==>', x, ' C:')


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lr = random.choice(list1)
print('Numero aleatorio de la lista ==>', lr)

nameList = ['juan', 'pedro', 'maria', 'jose', 'nico',
            'valen', 'santiago', 'pancho', 'joe', 'donal']
nr = random.choice(nameList)
print('Nombre aleatorio ==>', nr.capitalize())
