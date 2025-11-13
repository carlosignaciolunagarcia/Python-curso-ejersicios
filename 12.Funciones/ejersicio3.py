'''
Crear una funcion que pida dos numeros. Si el primero es mayor al segundo, 
el programa debe retornar el valor 1; si el segundo es mayor al primero, 
debe retornar -1; si ambos son iguales, debe retornar 0
'''

def function():
    num1=int(input("ingrese el primer numero"))
    num2=int(input("ingrese el segundo numero"))

    if num1>num2:
        print("El primer numero es mayor")
        return 1
    elif num2>num1:
        print("El segundo numero es mayor")
        return -1
    elif num2==num1:
        print("Los dos numero son iguales")
        return 0
    
resultado=function()