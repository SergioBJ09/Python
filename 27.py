def llegir_caracters():
    l=[]
    x=input("Introduce el año actual: ")
    l.append(x)
    for i in range(4):
        a=input("Año de nacimiento: ")
        l.append(a)
        l.append(int(x)-int(a))
        l.append(input("Nombre: "))
        
    return l

#PP
a=llegir_caracters()
print("""
Año Actual {}

Fecha de Nacimiento      Años que cumplira     Nombre

{}                        {}                 {}

{}                        {}                 {}

{}                        {}                 {}

{}                        {}                 {}
""".format(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10],a[11],a[12]))
