#40. Crea un programa que cuente todos los números pares hasta el número 50

pares=0
impares=0

for contador in range(1,51):
    if contador%2==0:
        pares+=1
    else:
        impares+=1

print(f"Números pares: {pares}")
print(f"Números impares: {impares}")