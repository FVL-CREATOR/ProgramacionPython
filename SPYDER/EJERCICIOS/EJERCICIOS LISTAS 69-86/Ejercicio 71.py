#71. Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en 
#esta lista no deben almacenarse las letras que se han introducido repetidas.
lista=[]
letras=0
repetir="s"

while repetir=="s":
    letras=input("Introduce una letra: ")
    repetir=input("¿Deseas repetir? s/n: ")
    lista.append(letras)
lista=set(lista)
print(lista)