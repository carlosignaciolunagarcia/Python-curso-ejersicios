'''
Imprimir por pantalla los numeros del 1 al 10, luego,
pedir al usuario dos numeros y mostrar el rango de numeros
entre ambas cifras
'''

for i in range (1,11):
    print(i)

indice1=int(input("indice 1:"))
indice2=int(input("indice 2:"))

for i in range (indice1,indice2 +1):
    print(i)