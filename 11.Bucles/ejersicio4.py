'''
Pedir al usuario que ingrese 2 numeros, después, se debe mostrar el rango
de esos 2 números, pero, solo imprimiendo los números que sean impares
'''

indice1=int(input("indice 1:"))
indice2=int(input("indice 2:"))

for i in range (indice1,indice2+1):
    if i%2!=0: 
        print(i)
