def menu(a):
    print("""
    Menu:
    1 - Dibujo 1
    2 - Dibujo 2
    0 - Salir
    """)

def crear_puntos(a):
    match a:
        case"1":
            print(
            """
              .  
             . . 
            .   .
             . . 
              .  
            """
            )
        case"2":
            print("""
            . . .
            . . .
            . . .
            """)
        case"3":
            print("""
            .....   .
                .   .
            .........
            .   .
            .   .....

            """)
        case"4":
            print("""
            .....
            .....
            ....................
            ....................
            ....................
            .....
            .....

            """)

popcio=menu
a=input("Elige una opción: ")
crear_puntos(a)