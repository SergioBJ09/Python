def leer_lista():
    l=[]
    for i in range(3):
        x=input("Introduce un numero: ")
        l.append(x)
    return l
def duplicados(a):
    aux=set(a)
    aux.update(a)
    if len(a)==len(aux):
        print("No hay duplicados")
    else:
        print("Hay un duplicado")

#PP
a=leer_lista()
duplicados(a)