def leer_numero():
    return input("Introduce un numero: ")
def suma_digitos(a):
    suma=0
    for e in a:
        suma+=int(e)
    if suma%2==0:
        print("La suma de los digitos de {} es {} y es par".format(a,suma))
    else:
        print("La suma de los digitos de {} es {} y es impar".format(a,suma))

#PP
a=leer_numero()
suma_digitos(a)