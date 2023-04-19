import random

def codigo():
    a=10
    b=10
    c=10
    d=10
    a1=random.randint(0,9)
    b1=random.randint(0,9)
    c1=random.randint(0,9)
    d1=random.randint(0,9)
    while a!=a1 or b!=b1 or c!=c1 or d!=d1:
        a=int(input("Introduce la primera cifra: "))
        b=int(input("Introduce la segunda cifra: "))
        c=int(input("Introduce la tercera cifra: "))
        d=int(input("Introduce la cuarta cifra: "))
        if a==a1:
            print("El primer numero es {}".format(a))
        elif a==b1 or a==c1 or a==d1:
            print("{} no esta bien colocado".format(a))
        else:
            print("{} no esta en el codigo".format(a))
        if b==b1:
            print("El segundo numero es {}".format(b))
        elif b==a1 or b==c1 or b==d1:
            print("{} no esta bien colocado".format(b))
        else:
            print("{} no esta en el codigo".format(b))
        if c==c1:
            print("El tercer numero es {}".format(c))
        elif c==a1 or c==b1 or c==d1:
            print("{} no esta bien colocado".format(c))
        else:
            print("{} no esta en el codigo".format(c))
        if d==d1:
            print("El cuarto numero es {}".format(d))
        elif d==a1 or d==b1 or a==c1:
            print("{} no esta bien colocado".format(d))
        else:
            print("{} no esta en el codigo".format(d))
        if a==a1 and b==b1 and c==c1 and d==d1:
            print("Correcto el codigo era {}{}{}{}".format(a,b,c,d))

#PP
y=codigo()