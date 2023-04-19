def rima():
    a=input("Inserte una palabra: ")
    b=input("Inserte una palabra para comprobar su rima con la primera: ")
    if len(a)<4 or len(b)<4:
        print("Utiliza palabras con mas letras")
    elif len(a)>3 and len(b)>3:
        if a[-3:]==b[-3:]:
            print("Tienen rima")
        elif a[-2:]==b[-2:]:
            print("Tienen un poco de rima")
        else:
            print("No tienen rima")

#PP
x=rima()