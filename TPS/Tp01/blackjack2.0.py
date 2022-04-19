import random

# Datos => numero de la carta , palos
print("---------\nBienvenido a BlackJack\n---------")

# Generacion de cartas del crupier
palos = ("Corazones", "Diamantes", "Treboles", "Picas")
palosRandom0 = random.choice(palos)
palosRandom1 = random.choice(palos)

deck = (2, 3, 4, 5, 6, 7, 8, 9, 10, "as", "j", "q", "k")
cartasCrupier0 = random.choice(deck)
cartasCrupier1 = random.choice(deck)
print(
    "El crupier tiene las siguientes cartas: ",
    cartasCrupier0,
    " de ",
    palosRandom0,
    " y ",
    cartasCrupier1,
    " de ",
    palosRandom1,
)

figura = False

# =========================================================

if cartasCrupier0 == "j" or cartasCrupier0 == "q" or cartasCrupier0 == "k":
    cartasCrupier0 = 10
    figura = True


elif cartasCrupier0 == "as":
    cartasCrupier0 = 11
# =========================================================
if cartasCrupier1 == "j" or cartasCrupier1 == "q" or cartasCrupier1 == "k":
    cartasCrupier1 = 10
    figura = True
elif cartasCrupier1 == "as":
    cartasCrupier1 = 11

sumaCrupier = cartasCrupier0 + cartasCrupier1

print("\nLa suma de sus cartas es:", sumaCrupier)


# Generacion Cartas Jugador
palosRandom2 = random.choice(palos)
palosRandom3 = random.choice(palos)

deck = (2, 3, 4, 5, 6, 7, 8, 9, 10, "as", "j", "q", "k")
cartasJugador0 = random.choice(deck)
cartasJugador1 = random.choice(deck)
print("---------")
print(
    "El Jugador tiene las siguientes cartas: ",
    cartasJugador0,
    " de ",
    palosRandom2,
    " y ",
    cartasJugador1,
    " de ",
    palosRandom3,
)

# =========================================================

if cartasJugador0 == "j" or cartasJugador0 == "q" or cartasJugador0 == "k":
    cartasJugador0 = 10
    figura = True
elif cartasJugador0 == "as":
    cartasJugador0 = 11
# =========================================================
if cartasJugador1 == "j" or cartasJugador1 == "q" or cartasJugador1 == "k":
    cartasJugador1 = 10
    figura = True
elif cartasJugador1 == "as":
    cartasJugador1 = 11

sumaJugador = cartasJugador0 + cartasJugador1

print("\nLa suma de sus cartas es:", sumaJugador)

# =========================================================
# Parte logica
print("---------\n")
# Toma de cartas si <=16

# -----------------------------------------------------

if sumaCrupier <= 16:
    print("El crupier tiene menos de 16, pide una carta.")

    palosRandom = random.choice(palos)
    cartasCrupier2 = random.choice(deck)

    print("La carta es:", cartasCrupier2, " de ", palosRandom)
    if cartasCrupier2 == "j" or cartasCrupier2 == "q" or cartasCrupier2 == "k":
        cartasCrupier2 = 10
        figura = True
    elif cartasCrupier2 == "as":
        cartasCrupier2 = 11

    sumaCrupier += cartasCrupier2
# -----------------------------------------------------
if sumaCrupier <= 16:
    print("El crupier tiene menos de 16, pide una carta.")

    palosRandom = random.choice(palos)
    cartasCrupier3 = random.choice(deck)

    print("La carta es:", cartasCrupier3, " de ", palosRandom)
    if cartasCrupier3 == "j" or cartasCrupier3 == "q" or cartasCrupier3 == "k":
        cartasCrupier3 = 10
        figura = True
    elif cartasCrupier3 == "as":
        cartasCrupier3 = 11

    sumaCrupier += cartasCrupier3

# -----------------------------------------------------
if sumaJugador <= 16:
    print("El Jugador tiene menos de 16, pide una carta.")

    palosRandom = random.choice(palos)
    cartasJugador2 = random.choice(deck)

    print("La carta es:", cartasJugador2, " de ", palosRandom)
    if cartasJugador2 == "j" or cartasJugador2 == "q" or cartasJugador2 == "k":
        cartasJugador2 = 10
        figura = True
    elif cartasJugador2 == "as":
        cartasJugador2 = 11

    sumaJugador += cartasJugador2
# -----------------------------------------------------
if sumaJugador <= 16:
    print("El Jugador tiene menos de 16, pide una carta.")

    palosRandom = random.choice(palos)
    cartasJugador3 = random.choice(deck)

    print("La carta es:", cartasJugador3, " de ", palosRandom)
    if cartasJugador3 == "j" or cartasJugador3 == "q" or cartasJugador3 == "k":
        cartasJugador3 = 10
        figura = True
    elif cartasJugador3 == "as":
        cartasJugador3 = 11

    sumaJugador += cartasJugador3


print('\nLa suma de las cartas del crupier es:', sumaCrupier,
      '\nLa suma de las cartas del jugador es:', sumaJugador)

if sumaCrupier > 21 and sumaJugador > 21:
    print('Ambos se pasan de 21, no hay un ganador. ')

elif sumaCrupier >= 17 and sumaJugador >= 17:
    print('Ambos tienen mas de 17, se plantan ambos.')
    if sumaCrupier > sumaJugador:
        if sumaCrupier > 21:
            print('\nEl jugador gana')
        else:
            print('\nEl crupier gana')
    elif sumaCrupier < sumaJugador:
        if sumaJugador > 21:
            print('\nEl crupier gana')
        else:
            print('\nEl jugador gana')
    elif sumaCrupier == sumaJugador:
        print('\nEmpate')
# ----------------------------------------------------- comprobación


if palosRandom0 == palosRandom2:

    if cartasCrupier0 == cartasJugador0:
        print('Las cartas son iguales')
    else:
        print('\nLos palos son iguales')

else:
    print("\nLos palos son diferentes")

if figura == True:
    print('\nAl menos salio una figura')
else:
    print('\nNo salio ninguna figura')
