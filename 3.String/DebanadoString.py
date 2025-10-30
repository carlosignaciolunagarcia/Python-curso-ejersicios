cadena= "este es un ejemplo de substring(Debanado de cadenas)"

#funcion len para saber el tamano del arreglo
print("Tamano del arreglo:",len(cadena))

print("Caracter de la cadena:",cadena[5])
print("debanado por rango:",cadena[0:12])
print("debanado por rango:",cadena[:12])
print("debanado por rango:",cadena[20:])
print("debanado al reves:",cadena[-2])

#-------------------------------------------------------------------

cadena= 'estoy utilizando los metodos de Python'
cadena2= 'ESTOY UTILIZANDO LOS METODOS DE PYTHON'

print(cadena.lower()) #pasa la cadena a minusculas
print(cadena2.lower())

print(cadena.upper())#pasa toda la cadena a mayusculas

print(cadena.capitalize())

print(cadena.title())# cambia a mayusculas cada inicio de palabr a

print(cadena.swapcase()) # invierte mayusca a minusculas y minusculas a muyusculas