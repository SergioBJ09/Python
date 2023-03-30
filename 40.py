def leer_numero():
    return (int(input("Introduce un numero: ")))

def tabla_multiplicar(a):
    for i in range(21):
        print("{}x{}={}".format(i,a,i*a))

#PP
a=leer_numero()
tabla_multiplicar(a)