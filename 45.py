def leer_lista():
    l=[]
    aux=[]
    for i in range(3):
        x=input("Introduce un numero: ")
        l.append(x)
        aux.append(x)
    return l,aux
def duplicados(a,aux):
    if aux[0]==(a[1] or a[2]):
        print("{} esta duplicado".format(aux[0]))
    elif aux[1]==(a[0] or a[2]):
        print("{} esta duplicado".format(aux[1]))
    elif aux[2]==(a[0] or a[1]):
        print("{} esta duplicado".format(aux[2]))
    else:
        print("No hay duplicados")



#PP
a,aux=leer_lista()
duplicados(a,aux)