'''
En la siguiente lista, debes hacer un programa que 
muestre los valores al usuario, a su vez, 
debe pedir dos datos y esos que sean ingresados 
deben ser sustituidos en el primer y segundo lugar:
[20, 50, "Curso", 'Python', 3.14]
'''

lista1=[20,50,"Curso","Python",3.14]
print("Elementos de la lista {}".format(lista1))

E1=input("Ingrese el primer dato:")
E2=input("ingrese el segundo dato:")

lista1[0]=E1
lista1[1]=E2

print("Elementos de la lista {}".format(lista1))