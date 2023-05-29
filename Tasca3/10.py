def division(a,b):
    try:
        r=a/b
    except ZeroDivisionError:
        print("Error, el segundo parametro es zero")
    else:
        print("El resultado de dividir {} entre {} es {}".format(a,b,r))

division(3,1)