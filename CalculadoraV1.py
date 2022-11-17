opcio=1
while(opcio!=0):
    print("""
    Menú:
    1. Numeros enteros
    2. Numeros Reales
    3. Cambios de Base
    0. Salir
    """
    )
    opcio=input("Seleccione la opcion que quiera: ")
    match opcio:
        case "1":
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
            a = input("Indique el primer operador: ")
            b = input("Indique el segundo operador: ")
            match opcio:
                case "1":
                    c=float(a)+float(b)
                    print("La suma de ",a," mas ",b," es ",c)
                case "2":
                    c=float(a)-float(b)
                    print("La resta de ",a," menos ",b," es ",c)
                case "3":
                    c=float(a)*float(b)
                    print("La multiplicación de ",a," por ",b," es ",c)
                case "4":
                    c=float(a)/float(b)
                    print("La división entre ",a," y ",b," es ",c)
                case "5":
                    c=float(a)//float(b)
                    print("El cociente de ",a," entre ",b," es ",c)
                case "6":
                    c=float(a)**float(b)
                    print("",a," elevado a ",b," es ",c)
                case "7":
                    c= float(a)%float(b)
                    print("El resto de ",a," entre ",b," es ",c)
                case "0":
                    print("Adios")   
                case other:
                    print("Opción no valida")