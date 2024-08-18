#Ejercisio 51: crear una tupla nmbradda parar representaar un punto en un lano.
#Invocacion de modlos nativos en python.

from collections import namedtuple
from math import sqrt

#class Punto:
#    def __init__(self,x,y):
#        self.x=x           #representacion comunde valores de modo class.         
#        self.y=y

Punto= namedtuple('Punto',['x','y'])

punto_1 =Punto(2,3)
punto_2 =Punto(-3,-5)

def calcular_distancia(punto_1, punto_2):
    return sqrt((punto_1.x-punto_2.x)**2+(punto_1.y-punto_2.y)**2)

print(calcular_distancia(punto_1,punto_2))