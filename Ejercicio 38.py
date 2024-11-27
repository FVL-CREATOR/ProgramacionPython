#38. A partir del programa anterior, establece los rangos para que el usuario no pueda introducir 
#notas inferiores a 0 y superiores a 10

num_notas=int(input("Introduce el número de notas que deseas introducir: "))

for contador in range (0,num_notas):
    notas=float(input("Introduce la nota: "))
    if notas>10 or notas<0:
        print("Has introducido una nota equivocada")
    elif notas>=5:
        print("Asignatura aprobada")
    elif notas<5:
        print("Asignatura suspendida")
    