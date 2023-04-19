def leer_lista():
    x='a'
    l=[]
    while x!='.':
        print("Introduce un '.' para parar de leer valores")
        x=input("Introduce un numero: ")
        if x!='.':
            l.append(x)
    return l
def duplicados(a):
    aux=set(a)
    aux.update(a)
    if len(a)==len(aux):
        print("No hay duplicados")
    else:
        print("{}, se han eliminado {} numeros".format(aux,len(a)-len(aux)))

#PP
a=leer_lista()
duplicados(a)