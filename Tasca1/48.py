def crear_llista_fitxer(ex48):
    with open(ex48, 'r') as fitxer:
        contenido=fitxer.read()
    lista=contenido.split()
    return lista
def leer_lista(x):
    lista_palabras=x("ex48.txt")
    print(lista_palabras)
#PP
x=crear_llista_fitxer()
leer_lista(x)