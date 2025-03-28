#BUCLES PRUEBA (1) EJER 49

var=input("Introduce la palabra secreta: ")
var1=input("Introduce una letra: ")

for contador in range (len(var)):
    
    if var1 in var[contador]:
        print("La letra se encuentra en la posición", contador+1)