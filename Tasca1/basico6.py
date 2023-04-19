def lista():
    x="a"
    l=[]
    while x!='0':
        x=input("Introduce un caracter: ")   
        if x!='0':
            l.append(x)
    return l
a=lista()
print(a)