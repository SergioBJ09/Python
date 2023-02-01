def llegir_caracters():
    l=[]
    for i in range(4):
        l.append(input("Introduce el año actual: "))
        aux=[]
        aux.append(input("Año de nacimiento: "))
        aux.append(input("Nombre: "))
        l.append(aux)
    return l

