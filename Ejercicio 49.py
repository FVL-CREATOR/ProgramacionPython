#49. A partir del programa anterior, modifica el código para que al introducir la letra por teclado te 
#indique en qué posición de la palabra se encuentra la letra.

var=input("Introduce la palabra secreta: ")
var1=input("Introduce una letra: ")

for contador in range (len(var)):
    
    if var1 in var[contador]:
        print("La letra se encuentra en la posición", contador+1)
        
    