#72. A partir del ejercicio anterior, se da por hecho que las vocales con o sin acento son repetidas y 
#no deben almacenarse en la lista

vocales_a=["a","á","à","A","Á","À"]
vocales_e=["e","é","è","E","É","È"]
vocales_i=["i","í","ì","I","Í","Ì"]
vocales_e=["o","ó","ò","O","Ó","Ò"]
vocales_e=["u","ú","ù","U","Ú","Ù"]

lista=[]

repetir=input("¿Deseas empezar s/n?: ")

while repetir=="s":
    letra=input("Introduce una letra: ")
    if letra in vocales_a:
        letra="a"
    if letra in  vocales_e:
        letra="e"
    lista.append(letra)
    repetir=input("¿Deseas continuar s/n?: ")
print(set(lista))