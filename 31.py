def vocales():
    x=input("Introduce una palabra: ")
    a=['a']
    a1=0
    e0=['e']
    e1=0
    i0=['i']
    i1=0
    o=['o']
    o1=0
    u=['u']
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
    print("{} tiene {} {}, {} {}, {} {}, {} {}, {} {}".format(x,a1,a,e1,e0,i1,i0,o1,o,u1,u))

#PP
a=vocales()
