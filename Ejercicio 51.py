#51. A partir del programa anterior, modifica el código para que sea el usuario quién introduzca el 
#número de veces que desea que repita la frase Buenos días. Con While

contador=int(input("Introduzca el numero de veces que quieres que se repita el bucle: "))

x=0
while x<contador:
    x=x+1
    print("Buenos días")
else:
    print("Programa terminado")
    