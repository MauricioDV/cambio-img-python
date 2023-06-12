import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import threading

print("Librerías Leídas")

# Crear la interfaz
ventana = tk.Tk()
ventana.title("Interfaz gráfica")
ventana.geometry('480x500')

# Crear los comandos
def mostrar_imagen():
    global imagen_actual, render  # Declarar la variable como global
    if imagen_actual == 1:
        img = Image.open('reloj1.jpg')
        imagen_actual = 2
    else:
        img = Image.open('reloj2.jpg')
        imagen_actual = 1

    new_img = img.resize((300, 256))
    render = ImageTk.PhotoImage(new_img)
    img_label.configure(image=render)
    ventana.after(10000, mostrar_imagen)  # 60000 milisegundos = 60 segundos

def leer_archivo():
    global imagen_actual  # Declarar la variable como global
    try:
        with open('texto.txt', 'r') as file:
            contenido = file.read().strip()
            if contenido == '1':
                imagen_actual = 1
            elif contenido == '2':
                imagen_actual = 2
    except FileNotFoundError:
        messagebox.showerror("Error", "El archivo texto.txt no se encontró.")

    mostrar_imagen()  # Llamar a mostrar_imagen() después de leer el archivo

def salir():
    if messagebox.askquestion("Salir", "¿Desea salir de la interfaz?") == 'yes':
        ventana.quit()
        ventana.destroy()

# Crear etiqueta para la imagen
img_label = Label(ventana)
img_label.place(x=10, y=30)

# Crear botones
boton1 = tk.Button(ventana, command=salir, text='Salir', height=2, width=20)
boton1.place(x=250, y=350)

# Iniciar la función de mostrar la imagen en segundo plano
imagen_actual = 1  # Inicializar la variable imagen_actual
render = None  # Inicializar render

leer_archivo()  # Llamar a leer_archivo() al inicio para establecer la imagen actual

ventana.mainloop()
