def llegir_caracters():
    l=[]
    for i in range(10):         #for i in range: Crea un bucle de (x) elementos
        l.append(input("Introduce un numero a la lista: ")) #append = Añadir al final de la lista
    return l

a=llegir_caracters()
suma=0
for e in a:             #for e in a: Lee la lista de uno en uno
    suma+=int(e)
print("la suma de todos es: ",suma)