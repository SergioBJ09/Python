def leer_numero():
    return (int(input("Introducir un valor: ")))
def leer_numero_float():
    return (float(input("Introducir un valor real: ")))
def calcular_prestamo(q,i,a):
    return (q*(1+i/100)**a)

#PP
q=leer_numero()
i=leer_numero_float()
a=leer_numero()
c=calcular_prestamo(q,i,a)
print("Si solicito {} en un interes aunal del {} de  {} años, al final pagare {} euros".format(q,i,a,c))