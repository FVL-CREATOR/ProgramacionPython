# Juego 7.5

import random
cartas=[1,2,3,4,5,6,7,10,11,12]
print("Te damos la bienvenida al juego del 7.5")

pregunta_juego="si"
while pregunta_juego=="si":
    punt_acum=0
    pregunta="si"
    while pregunta=="si":
        pregunta=input("¿Quieres una carta? (si/no): ").lower()
        if pregunta=="si":
            carta=random.choice(cartas)
            print("Tu carta es", carta)
            valor=0.5 if carta in [10, 11, 12] else carta
            punt_acum+=valor
            print("Tienes", punt_acum, "puntos acumulados")
            if punt_acum>7.5:
                print("Has perdido la partida")
                break
            if punt_acum==7.5:
                print("Enhorabuena, has ganado la partida")
                break
    if pregunta=="no":
        if 6<=punt_acum<=7:
            print("Has sido un poco conservador")
        elif punt_acum<6:
            print("Quizás tendrías que arriesgar un poco ¿no?")
    
    pregunta_juego=input("¿Quieres jugar otra partida? (si/no): ").lower()