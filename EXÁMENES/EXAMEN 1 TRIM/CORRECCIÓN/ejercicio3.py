total=0
cif=int(input("Introduzca el número de cifras: "))
var=input("Introduzca el número: ")
if len(var)!=cif:
    print("Error, no coincide el número de cifras")
else:
    for x in var:
        var1=int(x)
        total=total+var1
    print("Resultado:",total)