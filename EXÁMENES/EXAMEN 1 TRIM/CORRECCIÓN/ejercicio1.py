print("""****GASOLINERA***
1. Sin plomo 95
2. Sin plomo 98
3. Gasóleo A
4. Gasóleo A+
*****************""")
gas=int(input("Escoja el tipo de combustible: "))
litro=float(input("Introduzca el número de litros a repostar: "))
cS5=1.765
cS8=1.913
cGa=1.746
cGA=1.839
if gas==1:
    x=cS5*litro
    print("EL total a pagar es:",x)
if gas==2:
    x=cS8*litro
    total=round(x-x*10/100,2)
    print("El total a pagar es:",x,"y con el descuento quea en",total)
if gas==3:
    x=cGa*litro
    print("EL total a pagar es:",x)
if gas==4:
    x=cGA*litro
    total=round(x-x*12/100,2)
    print("El total a pagar es:",x,"y con el descuento queda en",total)