def sumar_lista(a):
    sumatorio=0
    for i in a:
        sumatorio+=i
    return sumatorio

def multiplicar_lista(lista):
    multiplicado=1
    for x in lista:
        multiplicado*=x
    return multiplicado

a=[1,2,3,9]
print("El sumatorio es: ",sumar_lista(a))
print("El producto es: ",multiplicar_lista(a))