def leer_lista():
    lista=[]
    a=0
    while a!='.':
        print("Introduce un '.' para parar de leer numeros")
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