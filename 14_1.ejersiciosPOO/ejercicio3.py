'''
Crear una clase Fabrica que tenga los atributos de Llantas, 
Color y Precio; luego crear dos clases mas que hereden de Fabrica,
las cuales son Moto y Carro. Crear metodos que muestren 
la cantidad de llantas, color y precio de ambos transportes. 
Por ultimo, crear objetos para cada clase y mostrar por pantalla 
los atributos de cada uno
'''

class Fabrica():
    def __init__(self,llantas,color,precio):
        self.llantas=llantas
        self.color=color
        self.precio=precio
    
    def cantidadllantas(self):
        print("Tengo {} llantas".format(self.llantas))

    def colorde(self):
        print("Tengo color {}".format(self.color))
    
    def preciode(self):
        print("Tengo un costo de: {}".format(self.precio))

class Moto(Fabrica):
    pass

class Carro(Fabrica):
    pass

moto=Moto(2,"azul",5000)
carro=Carro(4,"rojo",500000)

print("---------------Datos de la moto:----------------")
moto.cantidadllantas()
moto.colorde()
moto.preciode()

print("---------------Datos del carro:----------------")
carro.cantidadllantas()
carro.colorde()
carro.preciode()