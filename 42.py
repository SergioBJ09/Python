def leer_numero():
    return input("Introduce un numero: ")
def digito_pares(a):
    l=[]
    for e in a:
        if int(e)%2==0:
            l.append(e)
    print("Los digitos pares de {} son {}".format(a,l))



#PP
a=leer_numero()
digito_pares(a)