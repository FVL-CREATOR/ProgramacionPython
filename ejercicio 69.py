#69. Realiza un programa que permita introducir una cantidad exacta de números, cada número se 
#irá almacenando en una lista. El programa debe finalizar presentando por pantalla los números 
#ordenados de menor a mayor

lista=[]
veces=int(input("Introduce el numero de veces que quieras teclear un numero: "))
for x in range (0,veces):
    num=int(input("Introduce un numero: "))
    lista.append(num)
lista.sort()
print(lista)