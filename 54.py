def leer_lista():
    x='a'
    l=[]
    while x!='.':
        print("Introduce un '.' para parar de leer valores")
        x=input("Introduce un numero: ")
        if x!='.':
            l.append(x)
    return l
def elementos_pares(a):
    for i,e in enumerate(a):
        if i%2==0:
            print(e)



#PP
a=leer_lista()
elementos_pares(a)