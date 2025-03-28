#81. A partir de una lista definida, busca el método apropiado para que se visualice un valor de la 
#lista al azar.

import random
listapalabras=["casa","barco","gota","madera","agua","puente","pantalón"]
listaletras=[]
palabra=random.choice(listapalabras)
print(palabra)