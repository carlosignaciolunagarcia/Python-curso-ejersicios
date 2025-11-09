'''
Escribir un programa que pida un numero 
al usuario y muestre las tablas de multiplicar de ese numero
'''

numero=int(input("Ingrese un numero:"))
i=0
while i<=10 :
    print("{} x {} = {}".format(numero,i,numero*i))
    i+=1