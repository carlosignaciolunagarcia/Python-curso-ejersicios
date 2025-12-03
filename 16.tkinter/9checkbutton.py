import tkinter as tk

ventana =tk.Tk()
ventana.title("Check button")
ventana.geometry("500x500")

opcioVar=tk.IntVar()

checkOpciones=tk.Checkbutton(
    ventana,
    text="Desea recibir notificaciones",
    variable=opcioVar,
    onvalue=1,
    offvalue=0
)
checkOpciones.pack()

def mostrarEstado():
    if opcioVar.get()==1:
        resultado.config(text="Notificaciones Activadas")
        print(opcioVar.get())
    else:
        resultado.config(text="Notificaciones Desactivadas")
        print(opcioVar.get())

boton= tk.Button(ventana, text="Confirmar", command=mostrarEstado)
boton.pack()

resultado=tk.Label(ventana,text="")
resultado.pack()

ventana.mainloop()