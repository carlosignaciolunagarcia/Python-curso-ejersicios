diccionario={1:2,2:3,3:4}
diccionario2={4:5,6:7}

#Borrar en elemento especifico del diccionario
'''
print(diccionario)
diccionario.pop(3)
print(diccionario)
'''
#Borrar todo el diccionario
'''
print(diccionario)
diccionario.clear()
print(diccionario)
'''

#obtener el valor de una llave en especifico mediante un metodo
'''
print(diccionario)
print(diccionario.get(2))
'''

#agregar un nuevo elemento al diccionario
diccionario.setdefault(4,5)
print(diccionario)

#Modificar un elemento existente
diccionario.update(diccionario2)
print(diccionario)