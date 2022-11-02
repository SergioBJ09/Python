print("""
Menú:
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
        c=int(a)+int(b)
        print("La suma de ",a," mas ",b," es ",c)
    case "2":
        c=int(a)-int(b)
        print("La resta de ",a," menos ",b," es ",c)
    case "3":
        c=int(a)*int(b)
        print("La multiplicación de ",a," por ",b," es ",c)
    case "4":
        c=int(a)/int(b)
        print("La división entre ",a," y ",b," es ",c)
    case "5":
        c=int(a)//int(b)
        print("El cociente de ",a," entre ",b," es ",c)
    case "6":
        c=int(a)**int(b)
        print("",a," elevado a ",b," es ",c)
    case "7":
        c= int(a)%int(b)
        print("El resto de ",a," entre ",b," es ",c)
    case "0":
        print("Adios")           
    case other:
        print("Opción no valida")