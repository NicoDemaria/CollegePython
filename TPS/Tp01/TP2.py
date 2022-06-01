import random
from tkinter import N

# Funciones a implementar

def menu():
    print("\n------------------\nMenú Black Jack:\n1.Agregar dinero a su pozo\n2.Jugar una mano\n3.Salir\n------------------")

def apuestaPozo(pozo):
    pozoActual = pozo
    print(
        f"\nSu pozo actual es {pozoActual} le recordamos que el pozo no puede ser mayor a 100.000.")

    while True:
        suma = int(input("Ingrese su apuesta para sumar al pozo: "))
        if suma <= 0:
            print("La cantidad a agregar al pozo no puede ser negativa ni 0. \nIngrese un monto valido\n------------------")
        elif suma > 100000:
            print(
                "La cantidad tiene que ser menor a 100.000. \nIngrese un monto valido\n------------------")
        else:
            break

    pozo += suma

    if pozo <= 100000:
        print(f"Su pozo actual es {pozo}")
        input("\nPresione Enter para continuar...")
        return pozo
    else:
        print(
            f"\nSu pozo es mas de 100.000, no se pudo realizar la operación. Su pozo actual es: {pozoActual}")
        input("\nPresione Enter para continuar...")

def salir(pVictoria, rachaVictoria, bjNatural, montoMax, pApuesta, maxPerdida, name):
    print(
        f"1. Su porcentaje de victoria es: {pVictoria}%\n2. La racha mas larga de victorias de el crupier es: {rachaVictoria}\n3. Cantidad de manos que hubo blackjack natural: {bjNatural}\n4. Monto máximo del pozo: {montoMax}")
    print(
        f"5. Promedio de apuestas: ${pApuesta}\n6. Máxima pérdida: ${maxPerdida}\n\nGracias por su tiempo {name}. Lo esperamos nuevamente.")

def porcVictoria(win, loose):
    if win == 0 and loose == 0:
        return 0
    else:
        return (win * 100) / (win+loose)
    
def montoMax(montoMax, montoNuevo):
    if montoMax > montoNuevo:
        return montoMax
    else:
        return montoNuevo

def promApuesta(sumaApuesta, contadorApuesta):

    if contadorApuesta != 0:
        return sumaApuesta / contadorApuesta
    else:
        return 0

def valorCartas(carta, puntos):
    if carta == "j" or carta == "q" or carta == "k":
        carta = 10
    elif carta == "as" and puntos+11 > 21:
        carta = 1
    elif carta == "as":
        carta = 11

    return carta

def juegoCrupier(cartas):
    bandera = False

    puntos = 0
    palos = ("Corazones", "Diamantes", "Treboles", "Picas")
    palosRandomcarta1 = random.choice(palos)
    palosRandomcarta2 = random.choice(palos)
    deck = (2, 3, 4, 5, 6, 7, 8, 9, 10, "as", "j", "q", "k")
    carta1 = random.choice(deck)
    carta2 = random.choice(deck)

    print(cartas)
    print(
        f"Las cartas del crupier son: {carta1} de {palosRandomcarta1}")
    
    todasLasCartas = f"Las cartas del crupier son: {carta1} de {palosRandomcarta1}, {carta2} de {palosRandomcarta2}"
    
    carta1p = valorCartas(carta1, puntos)
    puntos += carta1p
    carta2p = valorCartas(carta2, puntos)
    puntos += carta2p
    if puntos == 21:
        bandera = True
        

    while puntos < 17:
        print(f"Tus puntos al momentos son: {puntos}")
        carta = random.choice(deck)
        paloRandom = random.choice(palos)
        print(f"--------------\nTu nueva carta es: {carta} de {paloRandom}")
        todasLasCartas += f", {carta} de {paloRandom}"
        cartaValue = valorCartas(carta, puntos)
        puntos += cartaValue

    print(
        f"-----------------\n Los puntos de el Crupier son: {puntos}\n-----------------")

    return puntos, bandera, todasLasCartas

def juegoJugador():
    bandera = False
    puntos = 0
    palos = ("Corazones", "Diamantes", "Treboles", "Picas")
    palosRandomcarta1 = random.choice(palos)
    palosRandomcarta2 = random.choice(palos)
    deck = (2, 3, 4, 5, 6, 7, 8, 9, 10, "as", "j", "q", "k")
    carta1 = random.choice(deck)
    carta2 = random.choice(deck)

    cartas = f"\nCartas del jugador: {carta1} de {palosRandomcarta1}, {carta2} de {palosRandomcarta2}"
    print(cartas)

    todasLasCartas = cartas
    carta1p = valorCartas(carta1, puntos)
    puntos += carta1p
    carta2p = valorCartas(carta2, puntos)
    puntos += carta2p
    if puntos == 21:
        bandera = True
        

    while puntos < 21:
        print(f"Tus puntos al momentos son: {puntos}")
        opcion = int(
            input("\nElija una opcion:\n1.Pedir otra carta\n2.Parar\nOpcion:"))
        if opcion == 1:
            carta = random.choice(deck)
            paloRandom = random.choice(palos)
            print(
                f"--------------\nTu nueva carta es: {carta} de {paloRandom}")
            cartaValue = valorCartas(carta, puntos)
            puntos += cartaValue
            todasLasCartas += f",{carta} de {paloRandom}"
        elif opcion == 2:
            break
        else:
            print("Elija una opción valida")

    print(f"-----------------\nTus puntos son {puntos}\n-----------------")

    return puntos, bandera, cartas, todasLasCartas

def mensajeDeRonda(pozo, apuesta, cartaJugador, puntajeJugador,cartaCrupier, puntosCrupier, ganador, nuevoPozo):
    print(f"-Monto inicial del pozo: {pozo}\n-Monto de la apuesta: {apuesta}\n-Cartas de Jugador: {cartaJugador}")
    print(f"-Puntaje de Jugador: {puntajeJugador}\n-Cartas crupier: {cartaCrupier}\n-Puntaje Crupier: {puntosCrupier}")
    print(f"El ganador fue: {ganador}\n-El monto actualizado del pozo es: {nuevoPozo}")

def ganador(puntosJugador, puntosCrupier, racha, rachaMax, apuesta, maxPerdida,victorias,derrotas,pozo,cartasJugador,cartasCrupier,banderaJ,banderaC):
    if puntosJugador > 21 or (puntosCrupier>puntosJugador and puntosCrupier<=21):
        print("\nHas perdido")
        maxPerdida = montoMax(apuesta, maxPerdida)
        racha += 1
        derrotas += 1
        nuevaRachaMax = montoMax(rachaMax, racha)
        nuevoPozo = pozo - apuesta
        ganador = "Crupier"
        mensajeDeRonda(pozo,apuesta,cartasJugador,puntosJugador,cartasCrupier,puntosCrupier,ganador,nuevoPozo)
        return maxPerdida, nuevaRachaMax,victorias,derrotas, racha, nuevoPozo
    elif puntosCrupier > 21 or puntosJugador>puntosCrupier:
        print("\nHas ganado")
        victorias+=1
        racha = 0
        nuevoPozo = pozo + apuesta
        ganador = "Jugador"
        mensajeDeRonda(pozo,apuesta,cartasJugador,puntosJugador,cartasCrupier,puntosCrupier,ganador,nuevoPozo)
        return maxPerdida, rachaMax,victorias,derrotas, racha, nuevoPozo
    elif puntosJugador == puntosCrupier and ((banderaC == False and banderaJ==False)or (banderaC and banderaJ)):
        print("Empate")
        ganador = "No hay ganadores es un empate"
        racha = 0
        nuevoPozo = pozo
        mensajeDeRonda(pozo,apuesta,cartasJugador,puntosJugador,cartasCrupier,puntosCrupier,ganador,nuevoPozo)
        return maxPerdida, rachaMax,victorias,derrotas, racha,pozo
    elif banderaJ:
        ganador = "Jugador por BlackJack Natural"
        victorias+=1
        racha = 0
        nuevoPozo = pozo + apuesta
        ganador = "Jugador"
        mensajeDeRonda(pozo,apuesta,cartasJugador,puntosJugador,cartasCrupier,puntosCrupier,ganador,nuevoPozo)
        return maxPerdida, rachaMax,victorias,derrotas, racha, nuevoPozo
    elif banderaC:
        maxPerdida = montoMax(apuesta, maxPerdida)
        racha += 1
        derrotas += 1
        nuevaRachaMax = montoMax(rachaMax, racha)
        nuevoPozo = pozo - apuesta
        ganador = "Crupier por BlacJackNatural"
        mensajeDeRonda(pozo,apuesta,cartasJugador,puntosJugador,cartasCrupier,puntosCrupier,ganador,nuevoPozo)
        return maxPerdida, nuevaRachaMax,victorias,derrotas, racha, nuevoPozo

def jugarUnaMano(pozo, sumaApuestas,contadorApuestas, blackJackNatural,rachaMax,maximaDerrota,derrota,racha,victorias,derrotas, montoMaxPozo):
    while True:
        apuesta = int(input("Ingrese un monto a Apostar multiple de 5: "))
        
        if apuesta % 5 == 0 and apuesta <= pozo:
            sumaApuestas += apuesta
            contadorApuestas += 1

            puntosJugador, banderaJugador, cartas, cartasJugador = juegoJugador()
            input("\nPresione Enter para continuar...")
            puntosCrupier, banderaCrupier, cartasCrupier = juegoCrupier(cartas)
            if banderaCrupier or banderaJugador:
                blackJackNatural += 1

            input("\nPresione Enter para continuar...")
            maximaDerrota, nuevaRachaMax, cant_victorias, cant_derrotas, laRacha,nuevoValorPozo = ganador(puntosJugador, puntosCrupier,racha,rachaMax,apuesta,maximaDerrota,victorias,derrotas,pozo,cartasJugador,cartasCrupier,banderaJugador,banderaCrupier)
            nuevoMontoMax =montoMax(pozo, nuevoValorPozo)
            input("\nPresione Enter para continuar...")
            return maximaDerrota, nuevaRachaMax, sumaApuestas, contadorApuestas, cant_victorias, cant_derrotas, laRacha, nuevoValorPozo,blackJackNatural, nuevoMontoMax
            
        elif apuesta > pozo:
            print(
                "No tiene suficiente dinero en el pozo. \nPuede agregar mas dinero en la opcion 1.")
            input("\nPresione Enter para continuar...")
            nuevoMontoMax = montoMax(montoMaxPozo, pozo)
            return maximaDerrota, racha, sumaApuestas, contadorApuestas, victorias, derrotas, racha, pozo,blackJackNatural, nuevoMontoMax
        elif apuesta % 5 != 0:
            print("Elija una apuesta que sea múltiplo de 5.\n-------------------")
        
# Constantes inicializadas:
pozo = 0
victorias = 0
derrotas = 0
apuestas = []
blackJackNatural = 0
montoMaxPozo = 0
racha = 0
maxRacha = 0
maximaDerrota = 0
cartas = ""
puntosJugador = 0
puntos = 0
sumaApuestas = 0
contadorApuestas = 0
derrota = 0
rachaMax = 0

# Inicio del Juego
print('\n"Bienvenido al Juego de BlackJack"\n-------------------')

name = input("Ingrese su nombre:")

pozo = apuestaPozo(pozo)
montoMaxPozo = pozo
# Ciclo while del Menu del Juego
while True:
    menu()
    menuOption = int(input("\nIngrese una Opción: "))

    if menuOption == 1:
        pozo = apuestaPozo(pozo)

    if menuOption == 2:
        maximaDerrota, maxRacha, sumaApuestas, contadorApuestas, victorias, derrotas, racha, pozo, blackJackNatural, montoMaxPozo = jugarUnaMano(pozo,sumaApuestas,contadorApuestas,blackJackNatural,rachaMax,maximaDerrota,derrota,racha,victorias,derrotas, montoMaxPozo)

    if menuOption == 3:
        print(f"Victorias = {victorias}")
        print(f"Derrotas= {derrotas}")
        salir(porcVictoria(victorias, derrotas), maxRacha, blackJackNatural,
              montoMax(montoMaxPozo, pozo), promApuesta(sumaApuestas, contadorApuestas), maximaDerrota, name)

        break

