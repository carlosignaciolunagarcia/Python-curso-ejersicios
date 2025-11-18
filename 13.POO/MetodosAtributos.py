class FabricaTelefonos():
    marca="Huawei"
    color="Negro"
    memoria=32
    alamacenamiento=128
    
    def llamar(self,mensaje):
        return mensaje

    def escucharMusica(self):
        print("Estas escuchando musica")

telefono=FabricaTelefonos()
telefono.marca
telefono.color
telefono.memoria
telefono.alamacenamiento
telefono.llamar("Hola, ¿Con quien hablo?")

print(telefono.alamacenamiento)
print(telefono.llamar("Hola, ¿Con quien hablo?"))
telefono.escucharMusica()