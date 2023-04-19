def gran(a,b):
    if(a>b):
        print(a, "es mayor que " ,b)
        return a
    elif(b>a):
        print(b, "es mayor que " ,a)
        return b
    else:
        print(a, "y" ,b, "tienen el mismo valor")
        return a

a=int(input("Numero 1: "))
b=int(input("Numero 2: "))
c=gran(a,b)