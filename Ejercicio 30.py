#30. Realiza un programa que controle si la longitud de una frase introducida por teclado es
#gual, menor o mayor de 11 caracteres. Utiliza elif

var1=input("Introduce una frase: ")
var2=(len(var1))
if var2==11:
    print("La frase tiene 11 caracteres")
elif var2<11:
    ("La frase tiene menos de 11 caracteres")
else:
    ("La frase tiene 11 o más caracteres")