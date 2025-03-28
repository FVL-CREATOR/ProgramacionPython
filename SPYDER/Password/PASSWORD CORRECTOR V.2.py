#3 numeros
#2 letras minusuclas
#1 letra mayuscula
#2 símbolos

cont_num=0
cont_let=0
cont_simb=0

max_num=3
max_let_mayus=1
max_let_minus=2
max_simb=2

password=input("Introducir un password: ")
error=True
for recorrer in password:
    if recorrer.isnumeric():
        cont_num+=1
    if recorrer.isupper:
        cont_let+=1
    if recorrer.islower:
        cont_let+=1
    if recorrer in "*_@&/#":
        cont_simb+=1

if cont_num<3:
    print(f"Faltan por introducir{max_num-cont_num} numeros ")
    error=False
if cont_let<3:
    print(f"Faltan por introducir{max_let-cont_let} letras ")
    error=False
if cont_simb<2:
    print(f"Faltan por introducir{max_simb-cont_simb} simbolos ")   
    error=False

if error==True:
    print("Correcto")
        