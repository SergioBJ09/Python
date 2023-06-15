import tkinter as tk
from tkinter import ttk
import random
# Crear la ventana principal
ventana = tk.Tk()
ventana.resizable(0,0)
# Definir la función que se ejecutará cuando se haga clic en el botón
def calcular(num1):
    a=1
def valor1(calc):
    calc
    imprimir(calc,num)
    return calc
def valor2(calc):
    calc.append(2)
    imprimir(calc,num)
    return calc
def valor3(calc):
    calc.append(3)
    imprimir(calc,num)
    return calc
def valor4(calc):
    calc.append(4)
    imprimir(calc,num)
    return calc
def valor5(calc):
    calc.append(5)
    imprimir(calc,num)
    return calc
def valor6(calc):
    calc.append(6)
def valor7(calc):
    return calc.append(7)
def valor8(calc):
    return calc.append(8)
def valor9(calc):
    return calc.append(9)
def valor0(calc):
    return calc.append(0)
def suma(calc,num):
    for e in calc:
        num.append(e)
    num.append("+")
    calc=()
def imprimir(calc,num):
    print(calc)
calc=()
num=()
boton1= tk.Button(ventana, text="1", command=valor1(calc), width=6, height=4).grid(row=1, column=0)
boton2= tk.Button(ventana, text="2", command=valor2(calc), width=6, height=4).grid(row=1, column=1)
boton3= tk.Button(ventana, text="3", command=valor3(calc), width=6, height=4).grid(row=1, column=2)
boton4= tk.Button(ventana, text="4", command=valor4(calc), width=6, height=4).grid(row=2, column=0)
boton5= tk.Button(ventana, text="5", command=valor5(calc), width=6, height=4).grid(row=2, column=1)
boton6= tk.Button(ventana, text="6", command=valor6(calc), width=6, height=4).grid(row=2, column=2)
boton7= tk.Button(ventana, text="7", command=valor7(calc), width=6, height=4).grid(row=3, column=0)
boton8= tk.Button(ventana, text="8", command=valor8(calc), width=6, height=4).grid(row=3, column=1)
boton9= tk.Button(ventana, text="9", command=valor9(calc), width=6, height=4).grid(row=3, column=2)
boton0= tk.Button(ventana, text="0", command=valor0(calc), width=18, height=4).grid(columnspan=2)
boton_enviar=tk.Button(ventana,text="=",width=6, height=4).grid(row=4, column=2)
ventana.mainloop()