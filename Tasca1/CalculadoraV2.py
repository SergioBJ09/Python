def menu_principal():
    print("""
    Menú:
    1. Numeros enteros
    2. Numeros Reales
    3. Cambios de Base
    0. Salir
    """
    )
    opcio=input("Seleccione la opcion que quiera: ")
    return opcio
def menu_enters():
    print("""
        Menú Calculadoras de Numeros Enteros:
        1. Sumar
        2. Restar
        3. Multiplicar
        4. Dividir
        5. Cociente
        6. Potencia
        7. Resto
        0. Salir
        """
        )
    opcio=input("Seleccione una opción: ")
    return opcio
def menu_reals():
    print("""
        Menú de Numeros Reales:
        1. Sumar
        2. Restar
        3. Multiplicar
        4. Dividir
        5. Cociente
        6. Potencia
        7. Resto
        0. Salir
        """)
    opcio=input("Seleccione una opción: ")
    return opcio
def menu_canvis_base():
    print("""
        Menú de Cambios de Base:
        1. Pasar Decimal a Binario, Octal y Hexadecimal
        2. Pasar Binario a Decimal, Octal y Hexadecimal
        3. Pasar Octal a Binario, Decimal y Hexadecimal
        4. Pasar Hexadecimal a Binario, Decimal y Octal
        """)
    opcio=input("Selecione la opcion que quiera: ")
    return opcio
def binario(a):
    binario= ' '
    while a // 2 !=0:
        binario = str (a % 2) + binario
        a = a // 2
        return str(a) + binario
#Fin Definiciones
opcio=1
while(opcio!=0):
    opcio=menu_principal()
    match opcio:
        case "1":
            opcio=menu_enters()
            a = int(input("Indique el primer operador: "))
            b = int(input("Indique el segundo operador: "))
            match opcio:
                
                case "1":
                    c=a+b
                    print("La suma de ",a," mas ",b," es ",c)
                case "2":
                    c=a-b
                    print("La resta de ",a," menos ",b," es ",c)
                case "3":
                    c=a*b
                    print("La multiplicación de ",a," por ",b," es ",c)
                case "4":
                    c=a/b
                    print("La división entre ",a," y ",b," es ",c)
                case "5":
                    c=a//b
                    print("El cociente de ",a," entre ",b," es ",c)
                case "6":
                    c=a**b
                    print("",a," elevado a ",b," es ",c)
                case "7":
                    c=a%b
                    print("El resto de ",a," entre ",b," es ",c)
                case "0":
                    print("Adios")   
                case other:
                    print("Opción no valida")
        case "2":
            opcio=menu_reals()
            a = float(input("Indique el primer operador: "))
            b = float(input("Indique el segundo operador: "))
            match opcio:
                case "1":
                    c=a+b
                    print("La suma de ",a," mas ",b," es ",c)
                case "2":
                    c=a-b
                    print("La resta de ",a," menos ",b," es ",c)
                case "3":
                    c=a*b
                    print("La multiplicación de ",a," por ",b," es ",c)
                case "4":
                    c=a/b
                    print("La división entre ",a," y ",b," es ",c)
                case "5":
                    c=a//b
                    print("El cociente de ",a," entre ",b," es ",c)
                case "6":
                    c=a**b
                    print("",a," elevado a ",b," es ",c)
                case "7":
                    c=a%b
                    print("El resto de ",a," entre ",b," es ",c)
                case "0":
                    print("Adios")   
                case other:
                    print("Opción no valida")
        case "3":
            opcio=menu_canvis_base()
            a=int(input("Indique el numero: "))
            match opcio:
                case "1":
                    b=a
                    c=a
                    d=a
                    print(" El numero ",b," en Binario es ",c,", en Octal ",d,", y en Hexadecimal ",d)
                case "2":
                    b=int(a,base=10)
                    c=int(a,base=8)
                    d=int(a,base=16)
                    print(" El numero ",a," en Decimal es ",b,", en Octal ",c,", y en Hexadecimal ",d)
                case "3":
                    b=int(a,base=2)
                    c=int(a,base=10)
                    d=int(a,base=16)
                    print(" El numero ",a," en Binario es ",b,", en Decimal ",c,", y en Hexadecimal ",d)
                case "4":
                    b=int(a,base=2)
                    c=int(a,base=10)
                    d=int(a,base=8)
                    print(" El numero ",a," en Binario es ",b,", en Decimal ",c,", y en Octal ",d)
        case "0":
            print("Adeu")
            opcio=0