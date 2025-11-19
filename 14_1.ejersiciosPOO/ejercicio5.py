'''
Crear un programa con tres clases Universidad, con atributos nombre 
(Donde se almacena el nombre de la Universidad). Otra llamada Carerra, 
con los atributos especialidad (En donde me guarda la especialidad de un estudiante). 
Una ultima llamada Estudiante, que tenga como atributos su nombre y edad. 
El programa debe imprimir la especialidad, edad, nombre y 
universidad de dicho estudiante con un objeto llamado persona.
'''
class Universidad():
    def __init__(self, nombreUniversidad):
        self.nombreUniversidad=nombreUniversidad

class Carrera():
    def __init__(self, especialidad):
        self.especialidad=especialidad

class Estudiante(Universidad,Carrera):
    def __init__(self,nombreUniversidad,especialidad ,nombreEstudiante, edadEstudiante):
        self.nombreEstudiante=nombreEstudiante
        self.edadEstudiante=edadEstudiante

        #llamado del los clases de las que se hereda
        Universidad.__init__(self,nombreUniversidad)
        Carrera.__init__(self,especialidad)
    
    def datosEstuduante(self):
        print("Alumno: {}".format(self.nombreEstudiante))
        print("Tengo: {} años".format(self.edadEstudiante))
        print("Mi universidad: {}".format(self.nombreUniversidad))
        print("Mi especialidad: {}".format(self.especialidad))
        
alumno=Estudiante("Ibero","ISC","Juan carlos",25)
alumno.datosEstuduante()