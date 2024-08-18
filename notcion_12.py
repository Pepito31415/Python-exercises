#Notacon 12:abstracion...

class Auto():
    def __init__(self):
        self.estado="apagado"

    def encender(self):
        self._estado="encendido"
        print("El auto esta ecendido")

    def conducir(self):
        if self._estado== "apagado":
            self.encender()
        print("Conducir el auto")

mi_auto=Auto()
mi_auto.conducir()