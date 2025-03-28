#25. Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos.

var1=float(input("Introduce tu nota: "))
if var1>10 or var1<0:
    print("ERROR")
    
if var1>=8.5 and var1<=10:
    print("Tu nota es",var1,", has sacado un excelente")
if var1>=6.5 and var1<8.5:
    print("Tu nota es",var1,", has sacado un notable")
if var1>=5 and var1<6.5:
    print("Tu nota es",var1,", has sacado un suficiente")
if var1<5:
    print("Tu nota es",var1,", has sacado un insuficiente")