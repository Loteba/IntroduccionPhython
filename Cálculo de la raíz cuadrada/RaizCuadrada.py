import tkinter as tk
from tkinter import messagebox
import math

def calcular_raiz():
    try:
        numero = float(entrada_numero.get())
        raiz = math.sqrt(numero)
        mensaje = f"La raíz cuadrada de {numero} es: {raiz}"
        messagebox.showinfo("Resultado", mensaje)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido")

# Crear la ventana
ventana = tk.Tk()
ventana.title("Calculadora de Raíz Cuadrada")

# Etiqueta y entrada para ingresar el número
tk.Label(ventana, text="Ingresa un número:").pack()
entrada_numero = tk.Entry(ventana)
entrada_numero.pack()

# Botón para calcular la raíz cuadrada
btn_calcular = tk.Button(ventana, text="Calcular Raíz Cuadrada", command=calcular_raiz)
btn_calcular.pack()

# Ejecutar la interfaz gráfica
ventana.mainloop()