print("****GASOLINERA****")
print("1. sin plomo 95")
print("2. sin plomo 98")
print("3. Gasóleo A")
print("4. Gasóleo A+")
opcion=int(input("Escoja el tipo de combustible: "))
litros=int(input("introduzca el numero de litros: "))
pagar1=0
pagar2=0
pagar3=0
pagar4=0
descuento1=0
descuento2=0
total1=0
total2=0
if opcion==1:
    pagar1=litros*1.765
    print("El total a pagar es:",pagar1)
if opcion==2:
    pagar2=litros*1.913
    descuento1=pagar2*0.10
    total1=pagar2-descuento1
    print("El total a pagar es:",pagar2,"y con el descuento queda en:",total1)
if opcion==3:
    pagar3=litros*1.746
    print("El total a pagar es:",pagar3)
if opcion==4:
    pagar4=litros*1.839
    descuento2=pagar4*0.12
    total2=pagar4-descuento2
    print("El total a pagar es:",pagar4,"y con el descuento queda en:",total2)