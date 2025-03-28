valor1=float(input("introduce el primer valor: "))
valor2=float(input("introduce el segundo valor: "))

Total1=valor2/valor1
Total2=valor1%2

print(f"el resultado de dividir (valor1) y (valor2) es: ", Total1)
print("el resto es: ", Total2)

if Total2==0:
    print("es par")
else:
    print("es impar")
