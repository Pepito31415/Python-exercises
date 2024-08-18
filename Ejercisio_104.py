#Ejercisio 104: crear una clase llamada estudiante que tenga como atributos 
# nombre, edad, grado, y que tenga cmo metodo de funcion "estudiar()" 
# el objeto tipo clase debe de interactuar con elusuario ademas 
# esta clase le debe de brindar al usuario iformacion de los diferentes atributos de la clase.

class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre= nombre
        self.edad= edad
        self.grado=grado

pedro= Estudiante("Pedro",23,3)

print(pedro.grado)