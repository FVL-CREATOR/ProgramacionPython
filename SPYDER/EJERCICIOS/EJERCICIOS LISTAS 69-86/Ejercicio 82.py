#82. Modifica el programa anterior para que sea el usuario intente adivinar la palabra escogida al 
#azar de la lista, indicando si es correcto o no. El programa debe no finaliza hasta que no se adivine 
#la palabra

import random
listapalabras=["casa","barco","gota","madera","agua","puente","pantalón"]
palabra=random.choice(listapalabras)
var1=input("Adivina la palabra: ")
while palabra!=var1:
    print("Sigue jugando")
    var1=input("Adivina la palabra: ")
else:
    print("Acertaste")