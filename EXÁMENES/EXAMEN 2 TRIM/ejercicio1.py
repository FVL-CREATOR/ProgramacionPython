lista=[]
var_num=int(input("Introduce 6 numeros separados por un guion: "))
lista_num=lista.append(var_num)

for recorrer in lista:
    var_total_num=len(var_num) 
maximo=max(var_num)
minimo=min(var_num)
promedio=sum(var_num)/var_total_num

print(f"El numero máximo de la lista es {maximo}")
print(f"El numero mínimo de la lista es {minimo}")
print(f"El promedio de todos los elementos de la lista es {promedio}")