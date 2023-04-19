def suma_todos():
    a=int(input("Introduce un numero: "))
    b=int(input("Introduce un segundo numero: "))
    suma=0
    for i in range(a,b+1):
        suma+=i
    print("La suma de todos los numeros desde {} hasta {} es {}".format(a,b,suma))


#PP
suma_todos()