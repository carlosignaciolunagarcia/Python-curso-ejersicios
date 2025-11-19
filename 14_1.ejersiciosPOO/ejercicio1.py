'''
Realizar un programa que conste de una clase llamada Estudiante, 
que tenga como atributos el nombre y la nota del alumno. 
Definir los métodos para inicializar sus atributos, imprimirlos y
mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
'''
class Estudiante():
    def __init__(self, nombre, nota):
        self.nombre=nombre
        self.nota=nota

    def imprimir(self):
        print("El alumno {} obtuvo la calificacion de {}".format(self.nombre,self.nota))

    def resultado(self):
        if self.nota>=6:
            print("HAS APROBADO!!!!")
        else:
            print("NO HAS APROBADO :(")

alumno=Estudiante("Juan carlos", 10)
alumno.imprimir()
alumno.resultado()