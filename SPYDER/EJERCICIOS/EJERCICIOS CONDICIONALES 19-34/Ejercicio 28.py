#28. Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza 
#elif.

var1=input("Introduce un término: ")

if var1.islower():
    print("La letra",var1,"es minuscula")
elif var1.isupper():
    print("La letra",var1,"es mayuscula")
elif var1.isnumeric():
    print("El valor introducido es un numero")
else:
    print("El término introducido es un símbolo")
    