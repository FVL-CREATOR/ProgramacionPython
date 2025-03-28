#31. Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. 
#Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su 
#índice. 

var1=("A quien madruga Dios ayuda: ")

palabras=("madruga", "Dios", "dios")

for palabra in palabras:
    indice=var1.find(palabra)
    if indice != -1:
        print(f'La palabra "{palabra}" está en la frase y se encuentra en el índice {indice}.')
    else:
        print(f'La palabra "{palabra}" está en la frase.')




