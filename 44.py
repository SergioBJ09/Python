def llegir_caracters():
    l=[]
    for i in range(3):
        l.append(input("Introduce un numero: "))
    return l
def orden(a):
    if a[0]>a[1] and a[1]>a[2]:
        print("Esta ordenado en orden descendente")
    elif a[0]<a[1] and a[1]<a[2]:
        print("Esta ordenado en orden ascendente")
    else:
        print("No esta ordenado")

#PP
a=llegir_caracters()
orden(a)
