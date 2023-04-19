import random
import time

# Funció on expliquem què passa
def intro():
    print ("""En una època on els gegants governen Menorca. Nosaltres necessitem menjar,
    Estem seguint el rastre de l'olor del menjar, però ens trobem en una cruïa.
    Al final de cada camí hi ha un talaiot, en un viuen els gegants bons que ens convidaran
    i en l'altre són uns caníbals afamats, i ens menjaran just ens vegin.
    """)

# Funció on demanem a quin talaiot volem anar
def canviTalaiot():
    talaiot = ""
    while talaiot != "1" and talaiot != "2":
        talaiot = input("A quin Talaiot vols anar? Introdueixi 1 o 2: ")
    return talaiot

# Funció que ens indica si compartiran el menjar o serem nosaltres el seu àpat
def trobada(canviTalaiot, puntos):
    p=puntos
    print ("T'estas apropant al talaiot...")
    time.sleep(2)
    print ("Està fosc i és tenebrós...")
    time.sleep(2)
    print ("Un gran gegant salta davant teu, t'agafa i ...")
    print ("")
    time.sleep(2)
    gegantamic = random.randint (1, 2)
    if canviTalaiot == str(gegantamic):
        p+=1
        print ("Et convida a menjar...")
        print("Has aconseguit 1 punts, tens {} punts".format(p))
    else:
        p-=1
        print ("Se't menja d'un mos...ÑAMÑAMÑAM")
        print("Has perdut 1 punts, tens {} punts".format(p))
    return p

# Funció principal 
partidaNova = ("si")
puntos=0
while partidaNova == ("s") or partidaNova == ("si"):
    intro()
    nTalaiot = canviTalaiot()
    puntos=trobada(nTalaiot, puntos)
    partidaNova = input("Vols tornar a mejar (jugar)? Introdueixi si o no: ")
    print("\n")
    
