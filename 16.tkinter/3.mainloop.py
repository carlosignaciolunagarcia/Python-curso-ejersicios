import tkinter as tk

ventana =tk.Tk()
ventana.title("mainloop")
ventana.geometry("500x500")
ventana.resizable(False,False) #Evita que la ventana se redimencione


marco = tk.Frame(ventana, width=300, height=200, bg="lightgray", borderwidth=2, relief="solid")
marco.pack_propagate(False) #evita que el marco (Frame) se redimencione
marco.pack(pady=50)

ventana.mainloop()