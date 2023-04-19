def es_primo(num):
    if num<2:
        return False
    for i in range(2,num):
        if num % i==0:
            return False
    return True
    


#PP
primos=[]
for i in range(1,101):
    if es_primo(i):
        primos.append(i)
        print(i)
print(len(primos))