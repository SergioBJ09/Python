def leer_lista():
    lista=[]
    a=0
    while a!='.':
        a=input("Introduce un numero: ")
        if a!='.':
            lista.append(a)
    return lista
def eliminarcapicua(a):
    l=[]
    l.append(a[1:-1])
    print(l)
#PP
a=leer_lista()
eliminarcapicua(a)