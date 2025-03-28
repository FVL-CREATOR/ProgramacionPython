#19. Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son 
#iguales

var1=int(input("Introduce el primer numero: "))
var2=int(input("Introduce el segundo numero: "))

if var1<var2:
    print("El numero",var1,"es menor que el numero", var2,)
elif var1>var2:
    print("El numero",var1,"es mayor que el numero", var2,)
elif var1==var2:
    print("Los numeros",var1,"y",var2,"son iguales")