
#Las variables necesitan la palbra clave "float" para saber que el usuario introduce un  numero real
var_1=float(input("Introduce el primer numero: "))
var_2=float(input("Introduce el segundo numero: "))

#No puede haber espacios entre palabras o numeros si no son indicados con "_"
var_total=var_1+var_2

#Aquí los errores está en las comas: la coma no puede ir después de la "f" porque su función ya es inútil y no tiene efecto y, para ello, hay que poner la coma después de las comillas.
print(f"el resultado de sumar var_1 y var_2 es:", var_total)
