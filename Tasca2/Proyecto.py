import random
def menu_principal():
    print("""
    Menú:
    1. Color Aleatorio
    2. Cuaderno de Contraseñas
    3. Blackjack
    4. Cronometro Externo
    0. Salir
    """
    )
    a=input("Seleccione la opcion que quiera: ")
    return a
def color_aleatorio():
    color=["Verde","Azul","Amarillo","Morado","Rojo","Negro","Blanco","Gris","Naranja","Marron","Rosa"] #Lista de Colores
    print("El color que ha salido ha sido {}".format(random.choice(color))) #Selecciona un elemento de la lista aleatoriamente y lo imprime
    input("Pulse ENTER para continuar")
def contraseña():
    d={}
    a=0
    while a!='.':
        print("Introduce un '.' para parar de leer numeros")
        a=input("Introduce tu usuario: ")
        
        if a!='.':
            b=input("Introduce tu contraseña: ")
            d[a]=b
    print("Las contraseñas guardadas son: {}".format(d))
    input("Pulsa ENTER para continuar")
def blackjack():
    a=1
    while a !=0:
        print("""
        Menú:
        1. Jugar
        0. Salir
        """)
        a=input("Seleccione una opcio: ")
        match a:
            case "1":
                cartas=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
                valores=[1,2,3,4,5,6,7,8,9,10,11,12,13]
                jugador=[]
                crupier=[]
                a=random.choice(cartas)
                a1=valores[a]
                b=random.choice(cartas)
                b1=valores[b]
                print("Tus cartas son: {} y {}, tienes un total de {}".format(a,b,a1+b1))
                
                print("""
                1 - Pedir Cartar
                2 - Plantarse
                """)
                opcio=input("Selecciona una opción: ")
                if opcio=="1":
                    c=random.choice(cartas)
                    c1=valores[c]
                    print("Tus cartas son : {}, {} y {}, tienes un total de {}".format(a,b,c,suma1+c1))
                    suma2=a1+b1+c1
                    jugador.append(suma2)
                if opcio=="2":
                    suma=a1+b1
                    jugador.append(suma)

                crupier1=random.choice(cartas)
                x=valores[crupier1]
                crupier2=random.choice(cartas)
                x1=valores[crupier2]
                if x+x1<10:
                    crupier3=random.choice(cartas)
                    x3=valores[crupier3]
                    suma3=crupier1+crupier2+crupier3
                    crupier.append(suma3)
                if x+x+1>10:
                    suma1=crupier1+crupier2
                    crupier.append(suma1)
                print("""
                Tu tienes {} y el Crupier tiene {}
                """.format(jugador,crupier))

                
                    
                  
def cronometro():
    a=0
#PP
opcio=1
while opcio!=0:
    a=menu_principal() #Lamamos al menu principal
    match a:
        case "1": #Si se introduce un 1 se ejecutara la función
            color_random=color_aleatorio()
        case "2": #Si se introduce un 2 se ejecutara la función
            cuaderno=contraseña()
        case "3": #Si se introduce un 3 se ejecutara la función
            juego=blackjack()
        case "4": #Si se introduce un 4 se ejecutara la función
            crono=cronometro()
        case "0":
            opcio=0
            print("Adios")
        case other:
            print("Opción Invalida")