#35. Programa que al introducir un número por teclado permita mostrar ese número de veces tu 
#nombre

numero=int(input("Introduce el  número de veces que quieres que salga por pantalla tu nombre: "))
nombre="Francesc Vivó López"

for contador in range (0,numero):
    print(nombre)