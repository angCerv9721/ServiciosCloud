#==================================================
#           Compara dos cadena largas 
#==================================================

doc1=open("llaveOriginal")#Colocar archvio en una linea
doc2=open("llaveCopia")#Colocar archivo en una linea
var1=doc1.read().rstrip('\n')
var2=doc2.read().rstrip('\n')
def comparacion (x,y):
    for i in range(0,len(x)):
        if (x[i]!=y[i]):
            print("\x1b[1;33m"+x[i], end='')
        else:
            print("\x1b[;37m"+x[i], end='')
    print("\n\n")

    for i in range(0,len(y)):
        if (i<len(x)):
            if (x[i]!=y[i]):
             print("\x1b[1;33m"+y[i], end='')
            else:
             print("\x1b[;37m"+y[i], end='')
        else:
            print("\x1b[1;33m"+y[i], end='')
    print("\n\n")

if (len(var1)<len(var2)):
    comparacion(var1,var2)
else:
    comparacion(var2,var1)