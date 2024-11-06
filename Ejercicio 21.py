#21. Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz 
#cuadrada no de un valor negativo

import math

a=int(input("Introduce el térimno a: "))
b=int(input("Introduce el térimno b: "))
c=int(input("Introduce el térimno c: "))


raiz=b**2-4*a*b
if raiz<0:
    print("No tiene solucion")
else:
    x1=-b+math.sqrt(b**2-4*a*b)/(2*a)
    x2=-b-math.sqrt(b**2-4*a*b)/(2*a)
    print("El valor de x1 es:",x1)
    print("El valor de x2 es:",x2)