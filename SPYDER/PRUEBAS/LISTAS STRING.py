#Contar el numero de palabras por separado...
lista=[]
frase=input("Introduce una frase: ")

#Cadena de texto a una lista (.split)
lista=frase.split()

palabra=input("Introduce la palabra a buscar: ")

print("El numero de palabras es", lista.count(palabra))      

#(.join) pasa de lista a string
frase1="-".join(lista)
print(frase1)