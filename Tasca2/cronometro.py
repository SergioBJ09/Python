import time
import threading
def cronometro(crono):
    segundos=0
    minutos=0
    tiempo=[]
    tiempo.append(minutos)
    tiempo.append(segundos)
    print(tiempo)
    while crono!='.':
        tiempo=[]
        segundos+=1
        if segundos==60:
            minutos+=1
            segundos=0
        tiempo.append(minutos)
        tiempo.append(segundos)
        time.sleep(1)
        print(tiempo)



        
#PP
timer_stop=threading.Event()
timer_stop.set()
t=threading.Thread(target=cronometro, args=(timer_stop,))
t.start
crono=input("Pulsa ENTER para comenzar el crono")
cronometro(crono)
time.sleep(5)
crono='.'
timer_stop.clear()
crono=input("Pulsa ENTER para comenzar el crono")

