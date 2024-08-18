#Ejercisio 37: Crear una jerarquia de herencia basica

#PErsona <- Estudiante

class Persona:
    def __inint__(self, documento,nombre, correo):
        self.dovumento=documento
        self.nombre=nombre
        self.edad=edad


class Estudiante(Persona):
    def __int(self,documento,nombre,correo,carnet,carrera):
        super().__init__(documento,nombre,correo)
        self.carnet=carnet
        self.carrera=carrera


german=Estudiante("123","German","pepitokungameer@gmail.com","987","programacion")#ERROR EN ESTA LINEA, BUSCAR ERROR MAS TARDE

print(isinstance(german,Estudiante))
print(isinstance(german,Persona))