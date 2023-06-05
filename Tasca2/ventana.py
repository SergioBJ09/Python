import time
import tkinter as tk
from tkinter import * #Importar el modulo y todos los atributos de TKinter
from tkinter import Tk, Button, Frame
import threading
from threading import Timer
from datetime import datetime
segundos=0
refresco=500
hora_inicio=0
def temporizador(segundos):
    segundos+=1
    return segundos
def hilo():
    hora_inicio=datetime.now()
    hilo1.start
    return hora_inicio
def numeros(segundos):
    horas = int(segundos / 60 / 60)
    segundos -= horas*60*60
    minutos = int(segundos/60)
    segundos -= minutos*60
    return f"{horas:02d}:{minutos:02d}:{segundos:02d}"
def obtener_tiempo_transcurrido_formateado():
    hora_actual=str(time())
    print(hora_actual)
    segundos_transcurridos=(hora_actual-hora_inicio)
    return numeros(int(segundos_transcurridos))
def refrescar():
    crono.set(obtener_tiempo_transcurrido_formateado)
    raiz.after(refresco,refrescar)
#PP
hora_inicio=hilo
hilo1=threading.Timer(1,function=temporizador(segundos))
raiz = Tk() #Creamos una clase "Raiz"
raiz.title("Cronometro") #Cambiar nombre de la Ventana
raiz.geometry("520x480") #Tamaño de la ventana
raiz.resizable(0,0) #Bloquea que se pueda editar el tamaño de la ventana
w=tk.Frame(raiz,width=320,height=160)
w.place(x=260,y=240)
boton=tk.Button(raiz,text="Start")
boton.config(command=hilo)
boton.place(x=150,y=200)
crono=tk.StringVar(raiz,value=obtener_tiempo_transcurrido_formateado())
raiz.tiempo=tk.Label(raiz,textvariable=crono,font=f"Consolas 60")
raiz.tiempo.pack(side="top")
app=tk.Frame()
refrescar()
app.pack()
app.mainloop() #Mantiene invisible la ventana "Raiz"
