#15. Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro,
#introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales.


radio = float(input("Introduce el valor del radio del cilindro: "))
altura = float(input("Introduce el valor de la altura del cilindro: "))

area_lateral=2 math.pi radio*altura
area_base=math.pi radio*2
area_total=area_lateral+2*area_base
volumen=area_base*altura

print("Área lateral del cilindro: area_lateral: ")
print("Área total del cilindro: area_total: ")
print("Volumen del cilindro: volumen: ")
