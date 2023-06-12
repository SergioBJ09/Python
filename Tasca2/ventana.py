import tkinter as tk
from tkinter import messagebox

def calculo(num1, operador, num2):
    num1 = float(num1)
    num2 = float(num2)
    resultado = 0
    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/":
        resultado = num1 / num2
    else:
        resultado = "Error"
    return resultado

def obtener_valores():
    num1 = entry_num1.get()
    operador = entry_operador.get()
    num2 = entry_num2.get()
    resultado = calculo(num1, operador, num2)
    messagebox.showinfo("Resultado", str(resultado))

raiz = tk.Tk()
raiz.title("Ventana")
raiz.resizable(0, 0)
entry_num1 = tk.Entry(raiz, width=6)
entry_num1.grid(row=0, column=0)
entry_operador = tk.Entry(raiz, width=2)
entry_operador.grid(row=0, column=1)
entry_num2 = tk.Entry(raiz, width=6)
entry_num2.grid(row=0, column=2)

boton = tk.Button(raiz, text="Enviar", command=obtener_valores)
boton.grid(row=1, column=0)
cerrar=tk.Button(raiz, text="Cerrar",command=raiz.destroy).grid(row=1,column=2)

raiz.mainloop()