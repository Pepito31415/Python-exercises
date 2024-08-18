#Herencia simple

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


roberto= Empleado("Roberto",42,"Argertino","programador",1000000)

herencia= issubclass(Empleado)
instancia= isinstance(roberto,Persona)

print(instancia)