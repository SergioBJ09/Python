def llegir():
    lista=[]
    a='a'
    while(a!='.'):
        a=input("Introdeix un nombre: ")
        if a!='.':
            lista.append(int(a))
    return tuple(lista)
def mostrar_majors_que(a,num):
    for e in a:
        if e>num:
            print(e)

#PP
x=llegir()
y=input("Introdeix el nombre que vols comparar: ")
mostrar_majors_que(x,int(y))