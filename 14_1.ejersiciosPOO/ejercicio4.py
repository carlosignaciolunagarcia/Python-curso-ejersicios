'''
Crear una clase llamada Marino(), con un metodo que sea hablar, 
en donde muestre un mensaje que diga "Hola...". Luego, 
crear una clase Pulpo() que herede Marino, pero modificar 
el mensaje de hablar por "Soy un Pulpo". Por ultimo, 
crear una clase Foca(), heredada de Marino, pero que tenga un atributo
nuevo llamado mensaje y que muestre ese mesjae como parametro
'''

class Marino():
    def __init__(self):
        pass

    def hablar(self):
        print("Hola...")

class Pulpo(Marino):
    def hablar(self):
        print("Soy un Pulpo")

class Foca(Marino):
    def __init__(self,mensaje):
        #super().__init__(self)
        self.mensaje=mensaje
    
    def hablar(self):
        print("mensaje:{}".format(self.mensaje))

#creacion de las instancias
pulpo=Pulpo()
foca=Foca("soy una foca")

#impresion de los mensajes
pulpo.hablar()
foca.hablar()