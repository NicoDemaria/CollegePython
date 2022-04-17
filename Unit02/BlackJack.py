import random

cartasDealer = random.randint(1, 10)
cartasJugador = random.randint(1, 10)

cartasDealer1 = random.randint(1, 10)
cartasJugador1 = random.randint(1, 10)

valorDealer = cartasDealer + cartasDealer1
valorJugador = cartasJugador + cartasJugador1

print('Si tenes 16 o menos, recibe otra carta, sino con 17 estoy obligado a plantarme')

print('Cartas del Dealer: ', valorDealer)
print('Cartas del Jugador: ', valorJugador)

sumatoriaDealer = random.randint(1, 10)
sumatoriaJugador = random.randint(1, 10)


if valorDealer <= 16 and valorJugador <= 16:
    print('Ambos piden una carta mas ')
    print('La carta de el dealer es: ', sumatoriaDealer,
          'La tercera carta de el jugador es: ', sumatoriaJugador)
    valorDealer += sumatoriaDealer
    valorJugador += sumatoriaJugador
    print('Los jugadores tienen ', valorDealer, ' y ', valorJugador)

elif valorDealer >= 17 and valorJugador >= 17:
    print('Ambos plantan', 'Sus cartas sos:', valorDealer, 'y', valorJugador)
elif valorDealer >= 17 and valorJugador <= 16:
    print('El Dealer planta, y el Jugador pide una carta mas')
    valorJugador += sumatoriaJugador
    print('El Jugador tiene ', valorJugador)
elif valorDealer <= 16 and valorJugador >= 17:
    print('El Jugador planta, y el Dealer pide una carta mas')
    valorDealer += sumatoriaDealer
    print('El Dealer tiene ', valorDealer)
elif valorDealer >= 17 and valorJugador >= 17:
    print('Ambos plantan, sus cartas son: ', valorDealer, 'y', valorJugador)
elif valorJugador <= 21:
    print('El Jugador gana')
elif valorDealer <= 21:
    print('El Dealer gana')
elif valorJugador >= 21:
    print('El Jugador se paso, el Dealer gana')
elif valorDealer >= 21:
    print('El Dealer se paso, el Jugador gana')
