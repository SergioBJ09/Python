def leer_lista():
    x='a'
    l=[]
    while x!='.':
        print("Introduce un '.' para parar de leer")
        x=input("Introduce una palabra: ")
        if x!='.':
            l.append(x)
    return l
def index_palabra(a):
    x=input("Introduce una palabra para indexear: ")
    for i,e in enumerate(a):
        if x==e:
            print("La palabra {} esta situada en {}".format(x,i))
        else:
            print("-1")



#PP
a=leer_lista()
index_palabra(a)