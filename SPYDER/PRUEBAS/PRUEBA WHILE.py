#Programa que te pida acertar un número secreto usando un bucle. El programa
#debe de finalizar en cuanto el usuario acierte.
import random
x=0
valor=random.randint(0,10)
while x<10:
    valorint=int(input("Introduce un número: "))
    if valorint==valor:
        x=10