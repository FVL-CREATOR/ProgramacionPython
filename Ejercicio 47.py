#47. Realiza un programa donde el usuario introduzca por teclado 2 intervalos, por pantalla se debe
#mostrar el rango de números teniendo en cuenta que se a<b la secuencia será incremental y si a>b
#la secuencia en descenso. Respeta el formato de salida

a=int(input("Introduce el primer número del intervalo (a): "))
b=int(input("Introduce el segundo número del intervalo (b): "))

if a<b:
    rango=range(a, b + 1)
else:
    rango=range(a, b - 1, -1)
    
for contador, num in enumerate(rango):
    if contador<len(rango) - 1:
        print(num, end="-")
    else:
        print(num)
