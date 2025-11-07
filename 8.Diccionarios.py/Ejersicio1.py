'''
En el siguiente diccionario se encuentran capitales de 
los paises en el mundo, debes realizar un programa que 
pida un pais al usuario, y muestre la capital de ese pais,
en dado caso el pais no este en el diccionario, se debe 
mostrar un mensaje diciendo que ese pais no se encuentra.
'''

Capitales={
    "Guatemala": "Ciudad de Guatemala",
    "El Salvador": "San Salvador",
    "Honduras": "Honduras",
    "Nicaragua": "Managua",
    "Costa Rica": "San Jose",
    "Panama": "Panama",
    "Argentina": "Buenos Aires",
    "Colombia": "Bogota",
    "Venezuela":"Caracas",
    "España": "Madrid"
}

Busqueda=input("Ingrese un pais:")

if(Busqueda.title() in Capitales):
    print("La capital de {} es: {}".format(Busqueda.capitalize(),Capitales[Busqueda.title()]))
else:
    print("País no se encuentra")
