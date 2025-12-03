import tkinter as tk

ventana =tk.Tk()
ventana.title("RadioButtom")
ventana.geometry("500x500")

def mostrarSeleccion():
    resultado.config(text=f"Opcion seleccionada: {seleccioVar.get()}")

seleccioVar=tk.StringVar()

opcion1=tk.Radiobutton(ventana,text="Opcion1", variable=seleccioVar, value="Opcion1")
opcion1.pack()

opcion2=tk.Radiobutton(ventana,text="Opcion2", variable=seleccioVar, value="Opcion2")
opcion2.pack()

opcion3=tk.Radiobutton(ventana,text="Opcion3", variable=seleccioVar, value="Opcion3")
opcion3.pack()

boton=tk.Button(ventana, text="Mostrar seleccion", command=mostrarSeleccion)
boton.pack()

resultado =tk.Label(ventana, text="")
resultado.pack()
ventana.mainloop()