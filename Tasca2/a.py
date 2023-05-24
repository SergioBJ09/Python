from datetime import datetime
import tkinter as tk
from tkinter import ttk
import time
import threading
INTERVALO_REFRESCO = 500  # En milisegundos
s=0
def segundos(s):
    s+=1
    return s
def threads():
    hilo1=threading.Timer(1, run(segundos(s)))
    hilo1.start()

hora_inicio = segundos(s)
start=0
def segundos_a_segundos_minutos_y_horas(s):
        m=0
        h=0
        if s==60:
            m=s/60
        if m==60:
            h=s/60/60
        return f"{h}:{m}:{s}"

def obtener_tiempo_transcurrido_formateado():
    s=hora_inicio
    return segundos_a_segundos_minutos_y_horas(s)


def refrescar_tiempo_transcurrido():
    variable_hora_actual.set(obtener_tiempo_transcurrido_formateado())
    raiz.after(INTERVALO_REFRESCO, refrescar_tiempo_transcurrido)
def comenzar():
    start=1
    print(start)
    return start


raiz = tk.Tk()
raiz.geometry("480x360")
raiz.title("Cronómetro")
variable_hora_actual = tk.StringVar(raiz, value=obtener_tiempo_transcurrido_formateado())
raiz.etiqueta = tk.Label(
    raiz, textvariable=variable_hora_actual, font=f"Consolas 60")
raiz.etiqueta.pack(side="top")
boton=ttk.Button(raiz,text="Start")
boton.config(command=threads())
boton.place(x=150,y=200)
app = tk.Frame()
refrescar_tiempo_transcurrido()
app.pack()
raiz.mainloop()
app.mainloop()