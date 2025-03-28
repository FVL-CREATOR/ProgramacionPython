#Ejercicio 2:
 
var_num=int(input("Introduce 6 cifras: "))

if var_num<0:  
    var_neg=0
if var_num>1234560:  
    var_pos=0
for contador in range(0,var_num):
    var_sum_pos=var_pos+1
    var_sum_neg=var_neg+1
print("La suma de valores positivos", var_sum_pos)
print("La suma de valores negativos", var_sum_neg)



