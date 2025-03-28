#BUCLES: PRUEBA (2) EJER 49

var=input("introduzca la palabra: ")

var1=input("dime una letra: ")
contador=0
for k in var:
    contador+=1
    if k==var1:
        print(f"la letra {var1} se encuentra en la posicion",contador)