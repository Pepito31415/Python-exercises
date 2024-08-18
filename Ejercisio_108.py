#Ejercisio 108: definir atributos y acciones de un animal a traves del metodo de MRO en forma de clases.

class Animal:
    def comer(self):
        print("El animal esta comiendo")

class Ave(Animal):
    def volar(self):
        print("el animal esta volando")

class mamifero(Animal):
    def amamantar(self):
        print("El animal esta amamantando")

class Murcuielago(mamifero,Ave):
    pass

murcielago = Murcuielago()

murcielago.comer()
murcielago.amamantar()
murcielago.volar()

print("-----------------------------------------------")

ave= Ave()

ave.comer()
ave.volar()