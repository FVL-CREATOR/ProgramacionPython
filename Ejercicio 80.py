#80. Utilizando listas, crea un programa que te permita determinar si un número es decimal o no.

lista=[]
numero=""

numero=input("Introduce un numero: ") 
lista=numero.split(".")
if len(lista)==2:
    print("Es un numero con decimales.")
else:
    print("No es un numero con decimales.")