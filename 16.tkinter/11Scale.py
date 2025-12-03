import tkinter as tk

def mostrarValor():
    resultado.config(text=f"Opcion seleccionada: {valorVar.get()}")

ventana =tk.Tk()
ventana.title("Scale")
ventana.geometry("500x500")

valorVar=tk.IntVar()

escala=tk.Scale(
    ventana,
    from_=0,
    to=100,
    orient=tk.HORIZONTAL,
    variable=valorVar
)
escala.pack()

boton=tk.Button(ventana, text="Mostrar valor", command=mostrarValor)
boton.pack()

resultado =tk.Label(ventana, text="")
resultado.pack()

ventana.mainloop()