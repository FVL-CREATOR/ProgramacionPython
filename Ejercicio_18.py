#18. Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan
#importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores
#de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por
#teclado el número de menores y el número de adultos que asisten al cine.

descuento_adulto=0.10  
descuento_menor=0.50   

num_adultos=int(input("Introduce el número de adultos: "))
num_menores=int(input("Introduce el número de menores: "))

total_adultos=num_adultos*precio_entrada*(1-descuento_adulto)
total_menores=num_menores*precio_entrada*(1-descuento_menor)

total_a_pagar=total_adultos+total_menores

print("El total a pagar es: total_a_pagar: euros")
