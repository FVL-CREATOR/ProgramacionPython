#Haced un programa que lea tres palabras a, b y c, i que escriba una linea con c, b y a en este orden.
concatenar=""
palabras=input()
lista=palabras.split()
for recorrer in lista:
    concatenar=recorrer+" "+concatenar
print(concatenar[:-1])
    