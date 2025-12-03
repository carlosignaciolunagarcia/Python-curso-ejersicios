import tkinter as tk 

#---------------------creamos la ventana--------------#
ventana = tk.Tk()
ventana.title("Menú")
ventana.geometry("500x500")

#---------------------creamos menu--------------#
menuBar = tk.Menu(ventana)
ventana.config(menu=menuBar)

#---------------------creamos la primera pestaña del menu--------------#
archivoMenu = tk.Menu(menuBar , tearoff=0)
menuBar.add_cascade(label="Archivo" , menu=archivoMenu)

#---------------------creamos el submenu de la primera pestaña--------------#
archivoMenu.add_command(label="Nuevo Archivo" , command=lambda: resultado.config(text="Nuevo Archivo"))
archivoMenu.add_command(label="Abrir Archivo" , command=lambda: resultado.config(text="Abrir Archivo"))
archivoMenu.add_command(label="Guardar Archivo" , command=lambda: resultado.config(text="Guardar Archivo"))
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir" , command=ventana.quit)

#---------------------creamos la segunda pestaña del menu--------------#
editarMenu = tk.Menu(menuBar , tearoff=0)
menuBar.add_cascade(label="Editar" , menu=editarMenu)
#---------------------creamos el submenu de la segunda pestaña--------------#
editarMenu.add_command(label="Cortar" , command=lambda: resultado.config(text="Cortar"))
editarMenu.add_command(label="Copiar" , command=lambda: resultado.config(text="Copiar"))
editarMenu.add_command(label="Pegar" , command=lambda: resultado.config(text="Pegar"))

resultado = tk.Label(ventana , text="")
resultado.pack()

ventana.mainloop()