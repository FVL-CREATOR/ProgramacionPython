#73. Diseña un programa que compruebe si los valores de la lista1 (casa,mesa,sal,sol,agua) están 
#repetidos o no en la lista2 (casa,luz,tres,tren,sol,pan). Haz que permita visualizar que palabras se 
#repiten y cuales no.

repetidas=""
norepetidas=""
lista1=["casa","mesa","sal","sol","agua"]
lista2=["casa","luz","tres","tren","sol","pan"]

for recorrer in lista2:
    if recorrer=="casa" or recorrer=="mesa" or recorrer=="sal" or recorrer=="sol" or recorrer=="agua":
        repetidas=repetidas+recorrer+(",")
    else:
        norepetidas=norepetidas+recorrer+(",")
print("Están repetidas", repetidas[:-1])
print("No están repetidas", norepetidas[:-1])