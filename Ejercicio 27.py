#27. Mejora el programa anterior para controlar que el valor introducido es una letra y en 
#caso de introducir un número, aparezca un aviso por pantalla

var1=input("Introduce un t�rmino: ")

if var1.islower():
    print("La letra",var1,"es minuscula")
if var1.isupper():
    print("La letra",var1,"es mayuscula")
if var1.isnumeric():
    print("El valor introducido es un numero")