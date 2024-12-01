#43. Realiza un programa que recorra con un for una palabra introducida por teclado y se imprima
#por pantalla cada letra


palabra=input("Introduce una palabra: ")

for contador in range(len(palabra)):
    print(f"En la posición {contador} está la {palabra[contador]}")
