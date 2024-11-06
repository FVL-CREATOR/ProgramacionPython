#32. Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para 
#no distinguir entre mayúsculas y minúsculas

var1=("A quien madruga Dios ayuda: ")

var2=var1.lower()

palabras=("madruga", "Dios", "dios")

for palabra in palabras:
    indice=var2.find(palabra.lower())
    if indice != -1:
        print(f'La palabra "{palabra}" se encuentra en el índice {indice}.')
    else:
        print(f'La palabra "{palabra}" no se encuentra en la frase.')
