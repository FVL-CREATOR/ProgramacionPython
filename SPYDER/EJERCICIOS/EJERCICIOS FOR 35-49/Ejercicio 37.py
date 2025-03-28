#37. Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado 
#o suspendido.

num_notas=int(input("Introduce el número de notas que deseas introducir: "))

for contador in range (0,num_notas):
    notas=float(input("Introduce la nota: "))
    if notas>=5:
        print("Asignatura aprobada")
    elif notas<5:
        print("Asignatura suspendida")
