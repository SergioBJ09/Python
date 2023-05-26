import tkinter as tk
from tkinter import * #Importar el modulo y todos los atributos de TKinter
from tkinter import ttk #Importa funciones adicionales de TKinter (El boton)
from tkinter import Tk, Button, Frame
import threading

class ventana:
    raiz = Tk() #Creamos una clase "Raiz"
    raiz.title("Cronometro") #Cambiar nombre de la Ventana
    raiz.geometry("520x480") #Tamaño de la ventana
    raiz.resizable(0,0) #Bloquea que se pueda editar el tamaño de la ventana
    w=tk.Frame(raiz,width=320,height=160)
    w.place(x=260,y=240)
    boton=ttk.Button(raiz,text="Start")
    boton.config()
    boton.place(x=150,y=200)
    raiz.mainloop()