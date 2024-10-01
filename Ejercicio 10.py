#10. Introduce por teclado dos números y muestre por pantalla la siguiente información: 

cociente, resto y si el dividendo es par o impar.
dividendo = int(input("Introduce el dividendo: "))
divisor = int(input("Introduce el divisor: "))

cociente=dividendo//divisor
resto=dividendo%divisor

print("cociente:", cociente)
print("resto:", resto)

if dividendo%2==0:
print("El dividendo es par.")
else:
print("El dividendo es impar.")
