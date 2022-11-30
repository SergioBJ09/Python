def caracter(x):
    vocales=["a","e","i","o","u","A","E","I","O","U"]
    if x in vocales:
        print("Verdadero")
    else:
        print("Falso")

x=input("Introduzca un caracter: ")
caracter(x)