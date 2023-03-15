def vocales():
    x=input("Introduce una palabra: ")
    a1=0
    e1=0
    i1=0
    o1=0
    u1=0
    for e in x:
        if e=='a':
            a1+=1
        if e=='e':
            e1+=1
        if e=='i':
            i1+=1
        if e=='o':
            o1+=1
        if e=='u':
            u1+=1
    print("{} tiene {} A, {} E, {} I, {} O, {} U".format(x,a1,e1,i1,o1,u1,))

#PP
a=vocales()
