#39. Programa que pida n números y que, tras introducir el último número, debe aparecer por 
#pantalla el número total de positivos, negativos y número de 0.

num_numeros=int(input("Introduce la cantidad de números que deseas introducir: "))

var_pos=0
var_neg=0
var0=0

for contador in range (0,num_numeros):
    numeros=int(input("Introduce un numero: "))
    if numeros>0:
        var_pos=var_pos+1
    elif numeros<0:
        var_neg=var_neg+1
    else:
        var0=var0+1
    
print("La cantidad de números positivos es:",var_pos)
print("La cantidad de números negativos es:",var_neg)
print("La cantidad de números ceros es:",var0)
