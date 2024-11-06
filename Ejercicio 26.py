#26. Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si 
#está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición.

var1=input("Introduce una letra: ")

if var1.islower():
    print("La letra",var1,"es minúscula")
if var1.isupper():
    print("La letra",var1,"es mayúscula")