#Ejercisio 114: principio de sustitucion de liskov(LSP):
#define una clase "Animal" con un metodos como "make_sound()" y "move()".
# crea clases derivadas como "dog", "cat", "bird" que cumplan con las mismas interfaces y comportamientos,

class Animal:
    def __init__(self, nombre, sonido, mover):
        self.nombre=nombre
        self.sonido=sonido
        self. mover=mover

    def ani_sonido(self):
        print(F"el {self.nombre} hace {self.sonido}")

    def ani_mover(self):
        print(f"El {self.nombre} esta {self.mover}")

class Dog(Animal):
    nombre="perro"
    sonido="guau"
    mover="moviendose"

class Cat(Animal):
    nombre="gato"
    sonido="miau"
    mover="moviendose"

class Bird(Animal):
    nombre="pajaro"
    sonido="*silbido*"
    mover="volar"

animal=Animal
perro=Dog
gato=Cat
pajaro=Bird

animal.ani_mover(self=perro)
animal.ani_sonido(self=perro)
animal.ani_mover(self=gato)
animal.ani_sonido(self=gato)
animal.ani_mover(self=pajaro)
animal.ani_sonido(self=pajaro)