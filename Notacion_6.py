#Notacion 6:Polimorfismo.

#propiedad de que en forma practica y multiple acceder y ejecutar diferentes objetos desde una funcion.

class Gato():
    def sonido(self):
        return "Miau"
    
class Perro():
    def sonido(self):
        return "guau"

def hacer_sonido(animal):
    print(animal.sonido())

gato= Gato()
perro=Perro()

hacer_sonido(gato)

print(gato.sonido())