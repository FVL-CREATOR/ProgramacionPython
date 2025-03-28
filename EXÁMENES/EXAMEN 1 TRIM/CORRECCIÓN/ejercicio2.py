posi=0
nega=0
for x in range(6):
    var=int(input("Introduce un número: "))
    if var>0:
        posi=posi+var
    else:
        nega=nega+var
print("Suma de números positivos:",posi)
print("Suma de números negativos:",nega)
        