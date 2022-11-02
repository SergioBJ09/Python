def menu_principal():
    print("""
    Calculadora
    Menu:
    1. Numeros enteros
    2. Numeros reales
    3. Canvis de base
    0. Sortir
    """)
    opcio=input("Selecciona l'opcio que vulgui: ")
    return opcio 

def menu_enters():
    print("""
            Menu Calculadora de nuemros enteros
            1. Sumar
            2. Restar
            3. Multiplicar
            4. Dividir
            5. Potencia
            6. Modul
            7. Cociente
            0. Sortir
            """)

    opcio=input("Selecciona l'opcio que vulgui: ")
    return opcio 

def menu_reals():
    print("""
            Menu Calculadora de nuemros enteros
            1. Sumar
            2. Restar
            3. Multiplicar
            4. Dividir
            5. Potencia
            0. Sortir
            """)

    opcio=input("Selecciona l'opcio que vulgui: ")
    return opcio 

def menu_canvis_de_base():
    print("""
            Menu Calculadora de cambios de base
            1. Pasar de decimal a binario, octal y hexadecimal
            2. Pasar de Binario a decimal, octal y hexadecimal
            3. Pasar de Octal a binario, decimal y hexadecimal
            4. Pasar de Hexadecimal a Binario, Octal y Decimal
            0. Sortir
            """)

def dectooctal(decimal):
    octal = " "
    while decimal > 0:
        residuo = decimal % 8
        octal = str(residuo) + octal
        decimal = int(decimal / 8)
    return octal
def dectobin(decimal):
    binario = " "
    while decimal > 0:
        residuo = decimal % 2
        binario = str(residuo) + binario
        binario = int(decimal / 2)
    return binario
def dectohex(decimal):
    hexadecimal = " "
    while decimal > 0:
        residuo = decimal % 16
        hexadecimal = str(residuo) + hexadecimal
        hexadecimal = int(decimal / 16)
    return hexadecimal

#Final Funciones
opcio=1
while(opcio!=0):
    opcio= menu_principal()
    match opcio:
        case "1":
            opcio2=menu_enters()
            a = int(input("Indiqui el primer operand: "))
            b = int(input("Indiqui el segon operand: "))

            match opcio:
                case "1":
                    c=int(a)+int(b) 
                    print("La suma de ",a," mes ",b," es ",c)
                case "2":
                    c=int(a)-int(b)
                    print("La resta de ",a," menys ",b," es ",c)
                case "3": 
                    c=int(a)*int(b)
                    print("La multiplicacio de ",a," per ",b," es ",c)
                case "4": 
                    c=int(a)/int(b)
                    print("La divisio de ",a," entre ",b," es ",c)
                case "5":
                    c= (a) ** (b)
                    print("La potencia de ",a," elevat a ",b," es ",c)
                case "6":
                    c= (a) % (b)
                    print("El modul de ",a," mòdul ",b," és ",c)
                case "7":
                    c= (a) // (b)
                    print("El cociente de ",a," entre ",b," es ",c)
                case "0": 
                    print("Adeu")
                case other:
                    print("opcion no valida")

        case "2":
            opcio=menu_reals()
            a = float(input("Indiqui el primer operand: "))
            b = float(input("Indiqui el segon operand: "))
                    
            match opcio:
                case "1":
                    c=int(a)+int(b) 
                    print("La suma de ",a," mes ",b," es ", c)
                case "2":
                    c=int(a)-int(b)
                    print("La resta de ",a," menys ",b," es ", c)
                case "3": 
                    c=int(a)*int(b)
                    print("La multiplicacio de ",a," per ",b," es ", c)
                case "4": 
                    c=int(a)/int(b)
                    print("La divisio de ",a," entre ",b," es ", c)
                case "5":
                    c= (a) ** (b)
                    print("La potencia de ",a," elevado a ",b," es ",c)
                case "0": 
                    print("Adeu")
                case other:
                    print("opcion no valida")

        case "3":
            opcio=menu_canvis_de_base()

            opcio =input("Indica la opcio que vulguis: ")
            a =input("Indiqui el nuombre: ")
                
            match opcio:
                case "1":
                    b=dectoocatal(a)
                    c=decto(a,base=10)
                    d=int(a,base=16)
                    print("El número ",a," en octal= ",b, " en decimal= ",c," en hexadecimal= ", d)
                case "2": # Octal a
                    b=int(a,base=2)
                    c=int(a,base=10)
                    d=int(a,base=16)
                    print("El número ",a," en binari= ",b, " en decimal= ",c," en hexadecimal= ", d)
                case "3": # Decimal a
                    b=dectobin(int(a))
                    c=dectooctal(int(a))
                    d=dectohex(int(a))
                    print("El número ",a," en binari= ",b, " en octal= ",c," en hexadecimal= ", d)
                case "4": # Hexadecimal a
                    b=int(a,base=2)
                    c=int(a,base=8)
                    d=int(a,base=10)
                    print("El número ",a," en binari= ",b, " en octal= ",c," en decimal= ", d)
                case "0":
                    print("Adéu")
                case other:
                    print("Opció no vàlida!")
        case "0":
            print("Adéu")
