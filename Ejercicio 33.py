#33. Programa un código que permita contar el número de vocales de la siguiente frase: No 
#hay mal que dure cien años

var1="No hay mal que dure cien años"

contador_vocales=0

vocales="aeiou"

for letra in var1:
    if letra in vocales:
        contador_vocales+=1

print(f'El número de vocales en la frase es: {contador_vocales}')
