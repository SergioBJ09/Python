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
    while a !="0":
        print("""
        Menú:
        1. Jugar
        0. Salir
        """)
        a=input("Seleccione una opcio: ")
        while a!="0":
            match a:
                case "1":
                    cartas=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
                    v=[1,2,3,4,5,6,7,8,9,10,11,12,13]
                    jugador=0
                    crupier=0
                    a=random.randint(0,12)
                    a1=v[a]
                    b=random.randint(0,12)
                    b1=v[b]
                    print("Tus cartas son: {} y {}, tienes un total de {}".format(cartas[a],cartas[b],a1+b1))
                    print("""
                    1 - Pedir Carta
                    2 - Plantarse
                    """)
                    opcio=input("Selecciona una opción: ")
                    if opcio=="1":
                        c=random.randint(0,12)
                        c1=v[c]
                        suma2=a1+b1+c1
                        jugador+=suma2
                        print("Tus cartas son : {}, {} y {}, tienes un total de {}".format(cartas[a],cartas[b],cartas[c],suma2))
                        input("Pulsa ENTER para continuar")
                    if opcio=="2":
                        suma=a1+b1
                        jugador+=suma

                    crupier1=random.randint(0,12)
                    x1=v[crupier1]
                    crupier2=random.randint(0,12)
                    x2=v[crupier2]
                    if x1+x2<10:
                        crupier3=random.randint(0,12)
                        x3=v[crupier3]
                        suma3=crupier1+crupier2+crupier3
                        crupier+=suma3
                    else:
                        suma1=crupier1+crupier2
                        crupier+=suma1
                    if crupier<10:
                        crupier4=random.randint(0,12)
                        x4=v[crupier4]
                        crupier+=crupier4

                    print("""
                    Tu tienes {} y el Crupier tiene {}
                    """.format(jugador,crupier))
                    if jugador<=21 and crupier<=21:
                        if jugador>crupier:
                            print("Has ganado")
                        elif crupier>jugador:
                            print("Has perdido")
                    if jugador>21 and crupier<=21:
                        print("Has perdido")
                    if crupier>21 and jugador<=21:
                        print("Has ganado")
                    if crupier==jugador or (crupier>21 and jugador>21):
                        print("Es un empate")
                    print("""
                    Volver a jugar?
                    1 - Volver a jugar
                    0 - Salir
                    """)
                    a=input("Introduce una opción: ")

                    


                
                    
                  
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