cadena=input('Ingresa tu nombre: ')
entero=int(input('ingresa tu edad: '))
flotante=float(input('ingresa tu peso(float): '))

#impresion del tipo y dato
print("tipo:",type(cadena),"valor:", cadena)
print("tipo:",type(entero),"valor:", entero)
print("tipo:",type(flotante),"valor:", flotante)

#otra forma de imprimir los datos es
print ("hola:{} tu edad es:{}".format(cadena,entero))