import random
# Datos => numero de la carta , palos
print('Bienvenido a BlackJack')
# Generacion de cartas del crupier
palos = ('Corazones', 'Diamantes', 'Treboles', 'Picas')
palosRandom = random.choice(palos)
palosRandom1 = random.choice(palos)

deck = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'as', 'j', 'q', 'k')
cartasCrupier = random.choice(deck)
cartasCrupier1 = random.choice(deck)
print('El crupier tiene las siguientes cartas: ', cartasCrupier,
      ' de ', palosRandom, ' y ', cartasCrupier1, ' de ', palosRandom1)

# =========================================================

if cartasCrupier == 'j' or cartasCrupier == 'q' or cartasCrupier == 'k':
    cartasCrupier = 10

elif cartasCrupier == 'as':
    cartasCrupier = 11
# =========================================================
if cartasCrupier1 == 'j' or cartasCrupier1 == 'q' or cartasCrupier1 == 'k':
    cartasCrupier1 = 10
elif cartasCrupier1 == 'as':
    cartasCrupier1 = 11

sumaCrupier = cartasCrupier + cartasCrupier1

print('\nLa suma de sus cartas es:', sumaCrupier)


# Generacion Cartas Jugador
palosRandom = random.choice(palos)
palosRandom1 = random.choice(palos)

deck = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'as', 'j', 'q', 'k')
cartasJugador = random.choice(deck)
cartasJugador1 = random.choice(deck)
print("---------")
print('El Jugador tiene las siguientes cartas: ', cartasJugador,
      ' de ', palosRandom, ' y ', cartasJugador1, ' de ', palosRandom1)

# =========================================================

if cartasJugador == 'j' or cartasJugador == 'q' or cartasJugador == 'k':
    cartasJugador = 10

elif cartasJugador == 'as':
    cartasJugador = 11
# =========================================================
if cartasJugador1 == 'j' or cartasJugador1 == 'q' or cartasJugador1 == 'k':
    cartasJugador1 = 10
elif cartasJugador1 == 'as':
    cartasJugador1 = 11

sumaJugador = cartasJugador + cartasJugador1

print('\nLa suma de sus cartas es:', sumaJugador)

# =========================================================
# Parte logica
if sumaCrupier <= 16 and sumaJugador <= 16:
    print('Ambos tienen menos de 16, piden cartas.')

    cartaJugador = random.choice(deck)
if cartaJugador == 'j' or cartaJugador == 'q' or cartaJugador == 'k':
    cartasJugador = 10
elif cartaJugador == 'as':
    cartasJugador = 11


cartaCrupier = random.choice(deck)

if cartaCrupier == 'j' or cartaCrupier == 'q' or cartaCrupier == 'k':
    cartaCrupier = 10
elif cartaCrupier == 'as':
    cartaCrupier = 11

sumaCrupier += cartaCrupier
sumaJugador += cartaJugador

print('\nLa suma de las cartas del crupier  es:', sumaCrupier,
      '\nLa suma de las cartas del jugador  es:', sumaJugador)
if sumaCrupier > sumaJugador:
    print('El crupier gana')
elif sumaCrupier < sumaJugador:
    print('El jugador gana')
else:
    print('Empate')

if sumaCrupier >= 17 and sumaJugador >= 17:
    print('Ambos tienen mas de 17, se plantan ambos.')
    if sumaCrupier > sumaJugador:
        print('El crupier gana')
    elif sumaCrupier < sumaJugador:
        print('El jugador gana')
    else:
        print('Empate')
