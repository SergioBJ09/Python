def llegir():
    l=[]
    a='a'
    while(a!='.'):
        a=input("Introdueix el nombre: ")
        if a!='.':
            l.append(a)
    return l
def nums_que_comencen_per(l,c):
    x=0
    p=[]
    for e in l:
        if e[0]=='a':
            x+=1
            p.append(e)
    print("El numero de paraules que comencen per A són {} i són {}".format(x,p))

#PP
a=llegir()
c='a'
nums_que_comencen_per(a,c)