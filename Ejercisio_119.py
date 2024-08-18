#Ejercisio 119: Principio de substitucion de liskov(LSP):
# Define una clase llamada "Vehicle" con metodos como "satrat_engine()" y "move()".
# crea clases derivadas como "car", "bicycle", y "Boat" que cumplan con las mismas interfases y 
# comportamientos.

class Vehicle:
    def __init__(self, vehicle):
        self.vehicle=vehicle
    def satrat_engiene(self):
        print("------------------------------")
        print("Encendiendo...")
        print(f"{self.vehicle} esta encendido")
    def move(self):
        print(f"El {self.vehicle} se esta moviendo")
        print("-------------------------------------")
    
class Car(Vehicle):
    vehicle="carro"

class Bicycle(Vehicle):
    vehicle="bicicleta"

class Boat(Vehicle):
    vehicle="bote"

veiculo=Vehicle
carro=Car
bici=Bicycle
bote=Boat

carro.satrat_engiene(carro)
carro.move(carro)
bici.satrat_engiene(bici)
bici.move(bici)
bote.satrat_engiene(bote)
bote.move(bote)