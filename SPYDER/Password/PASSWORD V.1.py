#Les primeres línies deL programa inviten a l´usuari a introduïr una contrasenya amb les següents instruccions.
print("Introdueix una contrasenya que contingui entre 6 i 8 caràcters i que segueixi les següents instruccions")
print("Posició 1: Un número major o igual que 1 i menor o igual que 5")
print("Posició 2: Una lletra minúscula")
print("Posició 3: Una lletra majúscula")
print("Posició 4: Un dels símbols *,_,@")
print("Posició 5: Una lletra minúscula")
print("Posició 6: Un número major o igual que 6 i menor o igual que 9")
print("Posició 7: Un dels símbols &,/,#")
print("Posició 8: Un número menor o igual que 5")

#Aquesta línia li demana a l´usuari que introdueixi una contrasenya per teclat seguint les instruccions citades anteriorment.
password=input("Introdueix una contrasenya: ")

#Ara afegeixo una variable que quan hi ha un error, aquest sigui vertader y quan no el hi hagi, sigui fals. A més, això és necessari perquè, en la majoria d´instruccions, utilitzaré el condicional "if not" i, per tant, sí o sí, hi ha d´haver un error diguent que si no es compleix el que es diu, hi hagi error.
error=False

#Ara toca dir-li al programa les instruccions que la contrasenya correcta ha de tenir amb condicionals i mètodes string. A més de dir-li a l´usuari que, si té algun error, el corregeixi en el caràcter que toca. El comptador de posicions comença a comptar des del 0, és a dir, que el caràcter 1 és el 0 per al programa.
#Amb aquesta primera instrucció, li dic al programa que vull que la longitud del password sigui de entre 6 i 8 caràcters.
if len(password)<6 or len(password)>8:
    print("Error, el password té una longitud de",len(password),"caràcters i no compleix els requisits.")

#Ara li dic al programa que el seu primer caràcter ha de ser numèric (mètode string ".isnumeric()"), entre 1 i 5 inclusive (variable "int" per a nombres enters). El condicional "elif" l´utilitzo per continuar amb la instrucció numèrica, però sense continuar amb el mètode string perquè ja està definit.
if not password[0].isnumeric():
        print("Error en el caràcter 1")
        error=True
elif int(password[0])<1 or int(password[0])>5:
        print("Error en el caràcter 1")
        error=True

#Amb aquesta tercera instrucció li dic al programa que el segon caràcter ha de ser una lletra minúscula, amb el mètode string ".islower()".
if not password[1].islower():
        print("Error en el caràcter 2")
        error=True

#Al tercer caràcter fem el mateix que amb el segon, però diguent-li al programa que la lletra ha de ser majúscul, utilitzant el mètode string ".isupper()".
if not password[2].isupper():
        print("Error en el caràcter 3")  
        error=True

#Aquesta instrucció ens serveix per indicar-li al programa que els únics símbols acceptats en aquest caràcter són "*,_,@". Això li indiquem amb dos iguals seguits per dir-li que estem comparant que si no es fa això, doni error.
if not password[3]=="*" and not password[3]=="_" and not password[3]=="@":
        print("Error en el caràcter 4")  
        error=True
        
#Com amb el segon caràcter, el cinquè ha de tenir una lletra minúscula.
if not password[4].islower():
        print("Error en el caràcter 5")  
        error=True
        
#Al igual que al caràcter 1, aquest ha de tenir un nombre entre 6 i 9 inclusive.
if not password[5].isnumeric():
        print("Error en el caràcter 6")
        error=True
elif int(password[5])<6 or int(password[5])>9:
        print("Error en el caràcter 6")
        error=True

#En aquest setè caràcter li demanem el mateix que al quart, però amb els següents símbols: "&,/,#". Aquí i al següent caràcter afegeixo el mètode string "len" perquè com que el password ha de tenir mínim 6 caràcters i, per tant, el setè i el vuité són opcionals, hi ha que posar un condicional que digui que si en el cas de que hi hagi més de 6 caràcters, aquests siguin opcionals.  
if len(password)>=7:    
    if not password[6]=="&" and not password[6]=="/" and not password[6]=="#":
            print("Error en el caràcter 7")  
            error=True

#En aquest últim caràcter opcional, es demana un nombre menor o igual que 5.
if len(password)>=8:
    if not password[7].isnumeric():
            print("Error en el caràcter 8")
            error=True
elif int(password[7])>5:
            print("Error en el caràcter 8")  
            error=True
#Per últim, li he de dir al programa que si els errors indicats en les instruccions anteriors no existeixen, són falsos i, per tant, el password és correcte i compleix amb els requisits.
if not error:
        print("El format del PASSWORD és correcte")