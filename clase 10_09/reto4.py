jugador1 = input("Jugada del jugador 1: ").lower()
jugador2 = input("Jugada del jugador 2: ").lower()

if jugador1==jugador2:
    print ("Hay un empate")
elif jugador1=="piedra" and jugador2=="tijera":
    print("Gana el jugador 1")
elif jugador1=="papel" and jugador2=="piedra":
    print("Gana el jugador 1")
elif jugador1=="tijera" and jugador2=="papel":
    print("Gana el jugador 1")
else:
    print("Gana el jugador 2")

