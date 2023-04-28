import time
import tkinter as tk
from tkinter import * #Importar el modulo y todos los atributos de TKinter
from tkinter import ttk #Importa funciones adicionales de TKinter (El boton)
from tkinter import Tk, Button, Frame

def cronometro():
    segundos=0
    minutos=0
    for i in range(10):
        tiempo=[]
        segundos+=1
        if segundos==60:
            minutos+=1
            segundos=0
        tiempo.append(minutos)
        tiempo.append(segundos)
        
        time.sleep(1)


#PP
raiz = Tk() #Creamos una clase "Raiz"
raiz.title("Cronometro") #Cambiar nombre de la Ventana
raiz.geometry("520x480") #Tamaño de la ventana
raiz.resizable(0,0) #Bloquea que se pueda editar el tamaño de la ventana
w=tk.Frame(raiz,width=320,height=160)
w.place(x=260,y=240)
boton=ttk.Button(raiz,text="Start")
boton.config(command=cronometro)
boton.place(x=150,y=200)
raiz.mainloop() #Mantiene invisible la ventana "Raiz"
cronometro()