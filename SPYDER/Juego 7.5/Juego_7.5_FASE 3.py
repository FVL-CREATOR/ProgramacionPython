import random

cartas=[1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,10,10,10,10,11,11,11,11,12,12,12,12]

saldo=100
rondas_jugadas=0

print("Te damos la bienvenida al juego del 7.5 con apuestas de dinero.")  
print("Tu saldo inicial es de 100€.")  

pregunta_partida=""
while pregunta_partida!="si" and pregunta_partida!="no":
    pregunta_partida=input("¿Quieres jugar una partida contra mí? (si/no): ").lower()
    if pregunta_partida!="si" and pregunta_partida!="no":
        print("Por favor, responde con 'si' o 'no'.")

if pregunta_partida=="si":
    alias=input("Genial, dime un alias con el que quieres que te llame durante toda la partida: ")  

#Una función adicional que he decidido añadir al programa es llamar "ronda" a un juego entre el jugador y la BANCA. Y llamaré "partida" al conjunto de rondas que se realicen mientras el jugador tenga saldo y deida seguir jugando. Esto lo hago para no generalizar la palabra "partida" y que pueda ser confuso.
while pregunta_partida=="si" and saldo>0:
    rondas_jugadas+=1  
    print("")
    print("----------------------------------")  
    print(f"         RONDA NÚMERO {rondas_jugadas}")  
    print("----------------------------------")  

    apuesta=-1
    while apuesta<=0 or apuesta>saldo:
        apuesta=input(f"{alias}, ¿cuánto quieres apostar en esta ronda? (Saldo:{saldo}€): ")
        if apuesta.isnumeric():
            apuesta=int(apuesta)
            if apuesta>saldo:
                print("No puedes apostar más de lo que tienes.")
        else:
            print("Introduce un número válido.")  
            apuesta=-1  
    print("")
    print("-------TURNO DEL JUGADOR-------")  

    punt_acum=0  
    pregunta_ronda="si"

    while pregunta_ronda=="si":
        carta=random.choice(cartas)
        print(f"Tu carta es {carta}")  
        valor=0.5 if carta in [10,11,12] else carta  
        punt_acum+=valor
        print(f"Tienes {punt_acum} puntos acumulados.")  

        if punt_acum>7.5:
            print("¡Vaya! Te has pasado de 7.5. Espera a ver el turno de la BANCA.")  
            break  

        if punt_acum==7.5:
            print("Enhorabuena! Has clavado el 7.5. ¡Eres un crack!")  
            break  

        pregunta_ronda=""
        while pregunta_ronda!="si" and pregunta_ronda!="no":
            pregunta_ronda=input("¿Quieres otra carta? (si/no): ").lower()
            if pregunta_ronda!="si" and pregunta_ronda!="no":
                print("Por favor, responde con 'si' o 'no'.")

    if pregunta_ronda=="no":
        if 6<=punt_acum<7:
            print("Has sido un poco conservador.")  
        elif punt_acum<6:
            print("Quizás tendrías que arriesgar un poco ¿no?")  

    print(f"Puntos acumulados de {alias}: {punt_acum}")
    print("")
    print("-------TURNO DE LA BANCA-------")  
    input("Pulsa Enter para ver la primera carta de la BANCA.")  

    punt_banca=0
    while punt_banca<7:
        carta=random.choice(cartas)
        valor=0.5 if carta in [10,11,12] else carta
        punt_banca+=valor
        print(f"BANCA ha sacado un {carta}. Puntuación de BANCA: {punt_banca}")  

        if punt_banca>7.5:
            print("BANCA se ha pasado.")  
            break

#Otra cosa que he querido añadirle al programa para que la BANCA no se vea tan escorada a intentar sacar siempre 7.5 y tener altas probabilidades de perder, he decidido hacer que si llega a 7, ya se puede plantar.
        if punt_banca>=6.5:
            print("BANCA se planta.")  
            break

        input("Pulsa Enter para que BANCA saque otra carta.")  

    print(f"Puntos acumulados de BANCA: {punt_banca}")  
    print("-------PUNTUACIÓN FINAL-------")  
    print(f"""{alias}: {punt_acum} puntos  
BANCA: {punt_banca} puntos""")  

    if punt_acum>7.5 and punt_banca<=7.5:
        print(f"{alias}, te has pasado y BANCA no. Pierdes {apuesta}€.")  
        saldo-=apuesta
    elif punt_acum<=7.5 and punt_banca>7.5:
        print(f"BANCA se ha pasado. ¡Ganas {apuesta}€!")  
        saldo+=apuesta
    elif punt_acum>7.5 and punt_banca>7.5:
        print(f"{alias}, los dos os habéis pasado. Pierdes {apuesta}€.")  
        saldo-=apuesta
    elif punt_acum==7.5 and punt_banca<7.5:
        print(f"¡Has conseguido 7.5! Ganas {apuesta}€.")  
        saldo+=apuesta
    elif punt_acum<7.5 and punt_acum>punt_banca:
        print(f"{alias}, ganas la ronda. Ganas {apuesta}€.")  
        saldo+=apuesta
    elif punt_acum<7.5 and punt_acum<punt_banca:
        print(f"BANCA gana. Pierdes {apuesta}€.")  
        saldo-=apuesta
    else:
        print("Empate. Recuperas tu apuesta.")  

    print(f"Tu saldo actual es: {saldo}€")  

    if saldo<=0:
        print(f"{alias}, te has quedado sin saldo. La partida ha terminado.")  
        break  

    pregunta_ronda=""
    while pregunta_ronda!="si" and pregunta_ronda!="no":
        pregunta_ronda=input(f"{alias}, ¿quieres jugar otra ronda? (si/no): ").lower()
        if pregunta_ronda!="si" and pregunta_ronda!="no":
            print("Por favor, responde con 'si' o 'no'.")  

    if pregunta_ronda=="no":
        print(f"Total de rondas jugadas: {rondas_jugadas}") 
        print(f"Gracias por jugar, {alias}. ¡La partida ha terminado!")   
        break