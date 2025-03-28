#36. Programa que sume los n primeros números naturales. n Lo introduce el usuario.

n=int(input("Introduce el numero de los primeros numeros naturales que quieres se sumen: "))
var1=0
for contador in range (0,n+1):
    var1=var1+contador
print("La suma de numeros es",var1)
