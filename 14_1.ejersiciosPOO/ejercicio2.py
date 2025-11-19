'''
Realizar un programa en el cual se declaren dos valores 
enteros por teclado utilizando el método __init__. Calcular 
después la suma, resta, multiplicación y división. Utilizar 
un método para cada una e imprimir los resultados obtenidos. 
Llamar a la clase Calculadora.
'''

class Calculadora():

    def __init__(self, v1=0, v2=0):
        self.v1=int(input("ingrese el valor entero:"))
        self.v2=int(input("ingrese el valor entero:"))

    def suma(self):
        print("resultado de la suma {} + {} es:{}".format(self.v1,self.v2,self.v1+self.v2))

    def resta(self):
        print("resultado de la resta {} - {} es:{}".format(self.v1,self.v2,self.v1-self.v2))

    def multiplicacion(self):
        print("resultado de la multiplicacion {} * {} es:{}".format(self.v1,self.v2,self.v1*self.v2))

    def divicion(self):
        print("resultado de la divicion {} / {} :{}".format(self.v1,self.v2,self.v1/self.v2))

operacion=Calculadora()
operacion.suma()
operacion.resta()
operacion.multiplicacion()
operacion.divicion()