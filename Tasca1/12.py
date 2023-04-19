def gran_tres(a,b,c):
    if(a>b):
        if(a>c):
            print(a, "es mayor que" ,b, "y" ,c)
            return a
        elif(a==c):
            print(a, "y" ,c, "tienen el mismo valor y son mayores que" ,b)
            return a,c
        else:
            print(c, "es mayor que" ,a, "y" ,b)
            return c
    if(b>a):
        if(b>c):
            print(b, "es mayor que" ,a, "y" ,c)
            return b
        elif(b==c):
            print(b, "y" ,c, "tienen el mismo valor y son mayores que" ,a)
            return b,c
        else:
            print(c, "es mayor que" ,a, "y" ,b)
            return c
    elif(a==b):
        if(a>c):
            print(a, "y" ,b, "tienen el mismo valor y son mayores que" ,c)
            return a,b
        elif(a==c):
            print(a,"," ,b, "y" ,c, "tienen el mismo valor")
            return a,b,c
        else:
            print(a, "y" ,b, "tienen el mismo valor y son menores que" ,c)
a=int(input("Numero 1: "))
b=int(input("Numero 2: "))
c=int(input("Numero 3: "))
d=gran_tres(a,b,c)
    