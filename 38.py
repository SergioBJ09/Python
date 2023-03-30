def leer():
    return input("Introduce un numero: ")
def recuento(a):
    x=0
    for e in a:
        x+=1
    print("{} tiene {} digitos".format(a,x))

#PP
a=leer()
recuento(a)