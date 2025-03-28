text=""
m=int(input("Var_min="))
M=int(input("Var_max="))
inter=int(input("Var_intervalo="))
for x in range(m,M+1,inter):
    var=str(x)
    text=text+var+","
print(text[0:len(text)-1])