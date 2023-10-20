#-----------------------------------------#
# Nombre: Mizael S.                       #
# Fecha: 20/10/2023                       #
#       Calculador de propinas UI         #
#-----------------------------------------#

import tkinter as tk
from tkinter import messagebox

def calcular_propina():
    try:
        subtotal = float(entry_subtotal.get())
        porcentaje_propina = float(entry_porcentaje_propina.get())
        propina = subtotal * (porcentaje_propina / 100)
        total = propina + subtotal
        mensaje = f"La propina aplicando {porcentaje_propina}% es de ${propina:.2f}, el total a pagar es de ${total:.2f}."
        messagebox.showinfo("Resultado", mensaje)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Propinas")

# Crear y colocar widgets
lbl_subtotal = tk.Label(ventana, text="Ingrese el monto de la factura total: ")
lbl_subtotal.grid(row=0, column=0, sticky=tk.W)
entry_subtotal = tk.Entry(ventana)
entry_subtotal.grid(row=0, column=1)

lbl_porcentaje_propina = tk.Label(ventana, text="Ingrese el % de propina: ")
lbl_porcentaje_propina.grid(row=1, column=0, sticky=tk.W)
entry_porcentaje_propina = tk.Entry(ventana)
entry_porcentaje_propina.grid(row=1, column=1)

btn_calcular = tk.Button(ventana, text="Calcular", command=calcular_propina)
btn_calcular.grid(row=2, columnspan=2)

# Iniciar el bucle principal de eventos
ventana.mainloop()
