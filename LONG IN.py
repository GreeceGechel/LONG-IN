from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
root = Tk()
root.geometry("400x300")
ventanaPrincipal = Frame(root)
ventanaPrincipal.grid()

titulo = Label(ventanaPrincipal,text="LONG IN",font=("Roboto",20))
titulo.grid(row=1, column=2)

titulo = Label(ventanaPrincipal,text="CONFIRMAR CONTRASEÑA",font=("Roboto",7))
titulo.grid(row=4, column=1)
textoConfirmarcontraseña = Entry(ventanaPrincipal, font=("Roboto",7))
textoConfirmarcontraseña.grid(row=4, column=2, padx=10, pady=10)


titulo = Label(ventanaPrincipal,text="HOMBRE",font=("Roboto",7))
titulo.grid(row=5, column=1)
titulo = Label(ventanaPrincipal,text="MUJER",font=("Roboto",7))
titulo.grid(row=5, column=2)
titulo = Label(ventanaPrincipal,text="ACEPTO TERMINOS",font=("Roboto",7))
titulo.grid(row=8, column=2)

control1=IntVar()
preserve1=Checkbutton(ventanaPrincipal, text="Hombre", variable=control1,font=("Roboto",10))
preserve1.grid(row=5,column=2,pady=1)

control2=IntVar()
preserve2=Checkbutton(ventanaPrincipal, text="Mujer", variable=control2,font=("Roboto",10))
preserve2.grid(row=5,column=3,pady=1)

botonIniciar = Button(ventanaPrincipal,text="Iniciar", command=root.destroy, width=15, height=2).grid(row=10, column=2)

root.mainloop()