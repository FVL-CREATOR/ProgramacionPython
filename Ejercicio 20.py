#20. A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados 
#números entre 0 y 10

var1=int(input("Introduce un numero entre el 0 y el 10: "))
var2=int(input("Introduce un segundo numero también entre el 0 y el 10: "))

if var1>10 or var1<0 or var2>10 or var2<0:
    print("Uno o los dos numeros estan fuera de los li�mites establecidos")
elif var1<var2:
    print("El numero",var1,"es menor que el numero", var2,)
elif var1>var2:
    print("El numero",var1,"es mayor que el numero", var2,)
elif var1==var2:
    print("Los numeros",var1,"y",var2,"son iguales")
    