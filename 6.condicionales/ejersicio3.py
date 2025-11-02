'''
Escribe un programa que pida dos palabras y
diga si riman o no. Si coinciden las tres 
últimas letras tiene que decir que riman. 
Si coinciden sólo las dos últimas tiene que 
decir que riman un poco y si no, que no riman.
'''
palabra1=input("ingrese la palabra 1:")
palabra2=input("ingrese la palabra 2:")

if len(palabra1)<3 or len(palabra2)<3:
    print("No rima, por que tienen menos de 3 aparacteres")
elif palabra1[-3:] ==palabra2[-3:]:
    print("las palabras riman")
elif palabra1[-2:] ==palabra2[-2:]:
    print("Las palabras riman un poco")
else:
    print("las palabras no riman")