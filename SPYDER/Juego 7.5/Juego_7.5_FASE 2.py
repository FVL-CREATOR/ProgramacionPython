import random

cartas=[1,2,3,4,5,6,7,10,11,12]
deposito=100

print("Te damos la bienvenida al juego del 7.5 con depósito de puntos.")

pregunta_juego="si"
while pregunta_juego=="si" and deposito>0:
    punt_acum=0
    pregunta="si"
    
    while pregunta=="si":
        pregunta=input("¿Quieres una carta? (si/no): ").lower()
        if pregunta=="si":
            carta=random.choice(cartas)
            print("Tu carta es", carta)
            valor=0.5 if carta in [10, 11, 12] else carta
            punt_acum+=valor
            print("Tienes", punt_acum, "puntos acumulados.")
            
            if punt_acum>7.5:
                print("Te has pasado de 7.5. Has perdido la partida y pierdes 10 puntos.")
                deposito-=10
                break
            if punt_acum==7.5:
                print("Enhorabuena, has ganado la partida y obtienes 10 puntos.")
                deposito+=10
                break

    if pregunta=="no":
        if 6<=punt_acum<=7:
            print("Te has plantado entre 6 y 7, ganaste 5 puntos.")
            deposito+=5
        elif punt_acum<6:
            print("Te has plantado con menos de 6, pierdes 5 puntos.")
            deposito-=5
    
    if deposito<=0:
        print("Tu depósito ha llegado a 0. Ya no puedes seguir jugando.")
        break
    
    print(f"Tu depósito actual es de {deposito} puntos.")
    if deposito>0:
        pregunta_juego=input("¿Quieres jugar otra partida? (si/no): ").lower()

print("Gracias por jugar. ¡Hasta la próxima!")
