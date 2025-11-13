'''
Crear un programa que tenga una lista, luego crear una funcion con la cual se van a pedir 
numeros al usuario para agregar a la lista. Debes crear una segunda funcion en donde se 
ordenen los numeros pares e impares dentro de dos listas nuevas
'''

def llenado():
    #Variables 
    arreglo=[]

    while True:
        opcion=int(input("¿Quiere ingresar un numero? \n1)si \n2)no \ningrese la opcion:"))
        if opcion==1:
            x=int(input("Ingrese su numero:"))
            #arreglo.insert(x)
            arreglo.append(x)
        elif opcion==2:
            print("arreglo completo:",arreglo)
            return arreglo
        else:
            print("Opcion invaliva favor de volverlo a intentar.\n\n")


def ordenar(arreglo):
    arreglo.sort()
    par=[]
    impar=[]
    for i in arreglo:
        if i%2==0:
            par.append(i)
        else:
            impar.append(i)
    print(par)
    print(impar)

arreglo1=llenado()
ordenar(arreglo1)