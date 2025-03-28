#Hacer listas de numeros, letras o mixtos entre corchetes. Mirar powerpoint

total=0
milista=[]
numero=int(input("Introduce un numero: "))

while numero!=0:
    milista.append(numero) #Append para añadir a la lista.
    numero=int(input("Introduce otro numero. Teclea 0 para salir: "))
print(milista)

#Valor maximo y minimo de la lista
print(max(milista))
print(min(milista))


#FORMA1 Sumar los numeros de la lista.
for recorrer in milista:
    total=total+recorrer
print(total)

#FORMA2 Sumar los numeros. Mas facil.
print(sum(milista))