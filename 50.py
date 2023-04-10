def lista():
    l=[]
    for i in range(1,11):
        l.append(i)
    return l
def inverso(a):
    a.sort(reverse=True)
    print(a)

#PP
a=lista()
inverso(a)