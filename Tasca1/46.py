import random

def leer_lista():
    l=[]
    for i in range(20):
        x=random.randint(1,100)
        l.append(x)
    l.sort()
    print(l)
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