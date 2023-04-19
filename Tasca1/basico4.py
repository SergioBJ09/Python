def leer():
    x=[]
    for i in range(10):
        x.append(int(input("Introduce un numero: ")))
    return x
a=leer()
y=0
for e in a:
    y+=e
print("El total es ", y)