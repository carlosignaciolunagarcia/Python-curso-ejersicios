diccionario={
    'Nombre':"Walter",
    'Apellido': "Coto",
    'Estatura': 1.8
}

#impresion de los datos
print(diccionario)

#solamente muestra las llaves
print(diccionario.keys())
print(diccionario.values())

#Impresion del valor de una clave en espesifico
print(diccionario["Estatura"])

#Agregar un nuevo valor al diccionario
diccionario["Peso"]="58 Kg"
print(diccionario)

#Modificar un valor ya existente
diccionario["Nombre"]="walter"
print(diccionario)