'''
Escribir una función que reciba un número entero positivo y devuelva su factorial.
'''
numero=int(input("ingrese un numero"))

def factorial (x):
    if x>=1:
        acumulado=x
        while x>=2:
            acumulado*=(x-1)
            x-=1
        return acumulado
    elif x==0:

        return 1    
    else:
        print("No hay factoriales negativos")
        return -1


resultado=factorial(numero)
print(resultado)