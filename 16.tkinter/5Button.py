import tkinter as tk

def cambiarTexto():
    mensajeCambiante.config(text="Texto cambiado")

def restablecertexto():
    mensajeCambiante.config(text="Mensaje original")

ventana =tk.Tk()
ventana.title("Button")
ventana.geometry("500x500")

etiqueta=tk.Label(ventana, text="Bottones")
etiqueta.pack()

etiqueta.config(text="Configuraciones:")

mensajeCambiante=tk.Label(ventana, text="Texto original")
mensajeCambiante.pack()

boton1=tk.Button(ventana,text="Cambiar texto", command=cambiarTexto)
boton1.pack()

boton2=tk.Button(ventana,text="Restablecer texto", command=restablecertexto)
boton2.pack()

ventana.mainloop()