#clases objetos.

class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca= marca
        self.modelo= modelo
        self.camara= camara

    def llamar(self):
        print(f"Estas haciendo una llamada desde: {self.modelo}")

    def cortar(self):
        print(f"estas cortando la llamada desde: {self.modelo}")        

celular1= Celular("Sansung","S23","48MP")
celular2= Celular("Appel","iphone 15 pro","96MP")

celular1.llamar()