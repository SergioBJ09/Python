def lista():
    par=[]
    impar=[]
    for i in range(1,101):
        if i%2==0:
            par.append(i)
        else:
            impar.append(i)
    return par,impar



#PP
par,impar=lista()
print("""
1 - Ver numero pares
2 - Ver numero impares
""")
x=input("Introduzca una opción: ")
match x:
    case "1":
        print(par)
    case "2":
        print(impar)
    case other:
        print("Opción invalida")