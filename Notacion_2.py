#Notacion 2: ejemplo y definicion de la herencia.

class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre= nombre
        self.edad=edad
        self.nacionalidad=nacionalidad

    def hablar(self):
        print("hola, estoy hablando un poco")

class Empleado(Persona):
    def __init__(self,nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo=trabajo
        self.salario= salario

class Estudiante(Persona):
    def __init__(self,nombre, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas=notas
        self.universidad=universidad

roberto= Empleado("Roberto",42,"Argertino", "rogramador",100000)

roberto.hablar()