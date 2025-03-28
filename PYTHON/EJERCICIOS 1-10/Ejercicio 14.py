import math

var_pi=math.pi

var_radio=int(input("Introduce el radio del circulo: "))

total=var_pi*(var_radio**2)

var_redondeo=round(total,2)

print(var_redondeo)
