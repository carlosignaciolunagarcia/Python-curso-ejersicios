class A():
    def __init__(self):
        self._cuenta=0
        self._contador=0
    
    @property
    def cuenta(self):
        return self._cuenta
    
    @cuenta.setter
    def cuenta(self, cuenta):
        self._cuenta=cuenta

    @cuenta.setter
    def contador(self, contador):
        self._contador=contador

    @property
    def contador(self):
        return self._contador

a=A()
#print(a._contador) #esta no es la forma correcta de llamr a un atributo

print(a.cuenta)
a.cuenta=20 #llamada metodo set
print(a.cuenta)

print(a.contador)
a.contador=10 #llamada al metodo set
print(a.contador)