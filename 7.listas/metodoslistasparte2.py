lista2=[5,3,1,4,2]

#busca y cuenta elementos que son iguales 
#a lo que se le pasa por el perentesis (cuantifica elementos)
print(lista2.count(5))

#regresa el indice del elemento que se busca
print("la posicion del elemento es:{}".format(lista2.index(4)))
print("ordenamiento: asendente")
print(lista2)
lista2.sort()
print(lista2)

print("ordenamiento: desendente:")
print(lista2)
lista2.reverse()
print(lista2)