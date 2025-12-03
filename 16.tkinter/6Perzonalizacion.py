import tkinter as tk

ventana =tk.Tk()
ventana.title("Personaliza Widgets")
ventana.geometry("500x500")

etiqueta=tk.Label(
    ventana, 
    text="Bienvenidad a Tkinter!", 
    bg="Lightblue", 
    fg="darkblue",
    width=50,
    height=4,
    font=("Helvetica",24,"italic")
)
etiqueta.pack(pady=25)

def actionBoton():
    etiqueta.config(text="Boton presionado", bg="green")
botton = tk.Button(
    ventana,
    text="Haz clic aqui",
    font=("Arial",20,"bold"),
    bg="orange",
    fg="white",
    activebackground="red",
    activeforeground="yellow",
    width=15,
    command=actionBoton
)

botton.pack()
ventana.mainloop()