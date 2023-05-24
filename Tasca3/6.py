def idempos(l):
    num=0
    for i,e in enumerate(l):
        if i==e:
            num=num+1
    return num
a=[0,1,2,3,5]
print("Hi ha {} numeros on coincideixen la posició i el numeros".format(idempos(a)))

def numi(l):
    return len([num for count, num in enumerate(l) if num==count])
print(numi([0,2,2,1,5,5,6,10]))