def lista():
    x="a"
    l=[]
    while x!='.':
        x=input("Introduce un numero: ")
        if x!='.':
            l.append(int(x))
    return l
a=lista()

