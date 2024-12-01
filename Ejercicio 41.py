#41. Imprime el siguiente patrón utilizando for:
    
for contador in range(5, 0, -1):
    for contador2 in range(contador, 0, -1):
        print(contador2, end="")
    print()