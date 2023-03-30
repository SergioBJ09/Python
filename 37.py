def leer_numero():
    return (int(input("Introduce un numero: ")))

def escape_sent(a):
    suma=0
    for i in range(a,1,-4):
        suma+=i*2
    print("La suma de los cuadrados separados entre si de {} es {}".format(a,suma))

#PP
a=leer_numero()
escape_sent(a)