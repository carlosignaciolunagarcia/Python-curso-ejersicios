import tkinter as tk

ventana =tk.Tk()
ventana.title("label")
ventana.geometry("500x500")

etiqueta=tk.Label(ventana, text="Hola, bienvenidad a Tkinter!")
etiqueta.pack()

etiqueta2=tk.Label(ventana, text="Hola, Este es el segundo label")
etiqueta2.pack()

ventana.mainloop()