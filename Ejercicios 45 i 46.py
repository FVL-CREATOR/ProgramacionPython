#45. Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el string
#distinguiendo vocales y las consonantes.

#46. A partir del programa anterior, soluciona el error que se produce en el test anterior con la
#palabra Abrigo utilizando únicamente una instrucción.


palabra = input("Introduce una palabra: ")

vocales = "aeiouáéíóúü"

vocales_encontradas = ""
consonantes_encontradas = ""

for letra in palabra.lower():
    if letra in vocales:
        vocales_encontradas += letra
    elif letra.isalpha():
        consonantes_encontradas += letra

print(f"Vocales: {vocales_encontradas}")
print(f"Consonantes: {consonantes_encontradas}")