#Ejercicio 2
cadena=input("Introduce una frase: ").lower()
lista=cadena.split()
print(lista)
palabra_buscada=input("Escoge la palabra que quieras buscar: ")
palabra_buscada_contar=lista.count(palabra_buscada)
print(f"La palabra que buscas se repite {palabra_buscada_contar} veces")
