class FabricaTelefonos():

    #constructor
    def __init__(self,marca,color):
        self.marca=marca
        self.color=color
        print("El objeto {} ha sido creado".format(self.marca))

    #str
    def __str__(self):
        return "El objeto es {}".format(self.marca)
    
    #destructor
    def __del__(self):
        print("El objeto {} ha sido destruido".format(self.marca))

telefono=FabricaTelefonos("Nokia","Negro")
print(telefono.marca)