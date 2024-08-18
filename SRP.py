#asignacion de funciones en diferentes clases.
class Tanque_de_combustible:
    def __init__(self):
        self.combustible = 100

    def agregar_combustible(self, cantidad):
        self.combustible += cantidad

    def obtener_combustible(self):
        return self.combustible

    def usar_combustible(self,cantidad):
        self.combustible -= cantidad

class Auto():
    def __init__(self, tanque):
        self.pocision=0
        self.combustible =tanque

    def mover(self,distancia):
        if self.tanque.obtener_combustible() >= distancia/2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia/2)
            print('Has movido el auto exitosamente')
        else:
            print("No hay suficiente combustible")
    
    def obtener_posicion(self):
        return self.obtener_posicion



tanque = Tanque_de_combustible()
auto = Auto(tanque)

print(auto)
print(auto.obtener_posicion())
print(auto.mover(10))
print(auto.obtener_posicion())
print(auto.mover(20))
print(auto.obtener_posicion())
print(auto.mover(60))
print(auto.obtener_posicion())
print(auto.mover(100))
print(auto.obtener_posicion())