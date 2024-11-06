#22. Programa que al introducir una nota por teclado te diga si has aprobado o suspendido. 
#Si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estás aprobado.

var1=float(input("Introduce tu nota: "))
if var1>10 or var1<0:
    print("ERROR")
elif var1>5:
    print("Has sacado un",var1,", has aprobado")
elif var1<5:
    print("Has sacado un",var1,", y has suspendido")
