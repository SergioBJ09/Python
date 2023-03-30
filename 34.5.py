import random

def calcula_n_random():
    b=[]
    for i in range(4):
        b.append(random.randint(0,9))
    return b
def leer_n_usuario():
    b=[]
    for i in range(4):
        b.append(int(input("Introduce un numero:")))
    return b
def comparar(a,b):
    todoigual=0
    existen=0
    for i in range(4):
        if a[i]==b[i]:
            todoigual+=1
        elif b[i] in a:
            existen+=1
        else:
            existen+=0
    return todoigual,existen


#PP
a=calcula_n_random()
salir=0
while salir!=1:
    b=leer_n_usuario()
    x,y=comparar(a,b)
    if x==4:
        print("Correcto, el codigo era {}".format(b))
        salir=1
    elif x<4 and y>0:
        print("Has adivinado {} numeros y hay {} que no estan bien colocados".format(x,y))
    elif x==0 and y>0:
        print("No has adivinado ningun numero y hay {} numeros que estan mal puestos".format(y))
    else:
        print("Ninguno de los numeros introducidos esta en el codigo")