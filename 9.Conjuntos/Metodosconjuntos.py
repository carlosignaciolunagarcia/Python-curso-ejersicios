conjunto = {1,1,2,3,3,4,4,5}
lista ={1,1,2,3,4,4}

print(lista) #imprime todo
print(conjunto) #imprime solo los valores unicos

#agregar un elemento al conjunto
print(conjunto)
conjunto.add(20)
print(conjunto)

#elimina un elemento al conjunto
print(conjunto)
conjunto.remove(1)
#conjunto.discard(1)
print(conjunto)

#elimina un elemento del conjunto al azar
print(conjunto)
conjunto.pop()
print(conjunto)

#eliminar
print(conjunto)
conjunto.clear()
print(conjunto)