#Ejercicio 1:
opcion1=print("1. Sin plomo 95")
opcion2=print("2. Sin plomo 98")
opcion3=print("3. Gasoleo A")
opcion4=print("4. Gasoleo A+")

var_gaso=input("Escoja el tipo de combustible: ")
var_litros=int(input("Introduzca el número de litros a repostar: "))

if var_gaso[opcion1]:
    var_precio=var_litros*1.765
    print("El total a pagar es", var_precio)
elif var_gaso[opcion2]:
     var_precio=var_litros*1.913
     print("El total a pagar es", var_precio)
elif var_gaso[opcion3]:
    var_precio=var_litros*1.746
    print("El total a pagar es", var_precio)
elif var_gaso[opcion4]:  
    var_precio=var_litros*1.839
    print("El total a pagar es", var_precio)
else:
    ("Error") 