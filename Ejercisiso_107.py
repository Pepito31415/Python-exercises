#Ejercisio 107: Herencia y su uso super.
# crear un sistema practico para una escuela.

class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

class Estudiante(Persona):
    def __init__(self,nombre, edad,grado):
        super().__init__(nombre,edad)
        self.grado=grado
    
    def mostrar_grado(self):
        print(f"Grado: {self.grado}")

estudiante= Estudiante("Juan","24", "decimo")
estudiante.mostrar_datos()
estudiante.mostrar_grado()