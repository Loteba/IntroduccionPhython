import tkinter as tk


def dibujar_cuadrado(canvas, x, y, lado, color):
    canvas.create_rectangle(x, y, x + lado, y + lado, fill=color)


def mover_cuadrado():
    global x, y, dx, dy

    x += dx
    y += dy

    canvas.delete("cuadrado")  # Borrar el cuadrado actual
    dibujar_cuadrado(canvas, x, y, lado, color="blue")  # Dibujar el cuadrado en la nueva posición

    ventana.after(100, mover_cuadrado)  # Mover el cuadrado cada 100ms


# Inicializar variables
x, y = 50, 50
lado = 100
dx, dy = 5, 3

# Crear la ventana
ventana = tk.Tk()
ventana.title("Cuadrado en Tkinter")

# Crear un lienzo donde dibujar
canvas = tk.Canvas(ventana, width=400, height=400)
canvas.pack()

# Dibujar el cuadrado en el lienzo
dibujar_cuadrado(canvas, x, y, lado, color="blue")

# Mover el cuadrado
mover_cuadrado()

# Ejecutar la interfaz gráfica
ventana.mainloop()