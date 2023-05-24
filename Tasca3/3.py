def llbc(ll,c):
    n=[]
    for x in ll:
        if x[:1]==c:
            n.append(x)
        return n
print(llbc(["sabo","taula","teclat","ratoli","tren"],"s"))



def a(lista,x):
    list(filter(lambda a:a[:1]==x,lista))
print(a(["Aroa","Ainhoa","Aram","Adria","Sergi","David","Ignasi"],"S"))