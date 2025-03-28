#84. A partir de la lista definida en el ejercicio 81, haz que se visualice por pantalla una de las 
#palabras, pero con todas sus letras desordenadas. El usuario tendrá que recolocar y acertar la 
#palabra secreta. El usuario tendrá 3 oportunidades para adivinar la palabra. 

import random
listapalabras=["casa","barco","gota"]
listaletras=[]
palabra=random.choice(listapalabras)
listadesorden=[]
palabradesordenada=0
#lo mismo que la siguiente
#for recorrer in palabra:
#    separada="-".join(palabra)
#   listaletras=separada.split("-")

while len(listaletras)>0:
    letra=random.choice(listaletras)
    listadesorden.append(letra)
    listaletras.remove(letra)
palabradesordenada="-".join(listadesorden)
print("Adivina la palabra",palabradesordenada)
usuario=input("Introduce la palabra: ")
while usuario!=palabra:
    print("error")
    usuario=input("Introduce la palabra: ")
else:
    print("Bien")