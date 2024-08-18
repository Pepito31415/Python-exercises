#Notacion 3: ejemplos y deffinicion de herencia multiple.

class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre= nombre
        self.edad=edad
        self.nacionalidad=nacionalidad

    def hablar(self):
        print("hola, estoy hablando un poco")

class Artista:
    def __init__(self,habilidad):
        self.habilidad=habilidad
    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad}"
        

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

class EmpleadoArtista(Persona,Artista):
    def __init__(self, nombre,edad,nacionalidad,habilidad,salario,empresa):
            Persona.__init__(self,nombre, edad, nacionalidad)
            Artista.__init__(self,habilidad)
            self.salario=salario
            self.empresa=empresa
    
    def presentarse(self):
        print(f"Hola soy {self.nombre}, {self.mostrar_habilidad()} y trabajo en {self.empresa}")

roberto= EmpleadoArtista("Roberto",42,"Argertino","cantar",1000000,"Cocacola")

herencia= issubclass(Empleado,Artista)
instancia= isinstance(roberto,Persona)

print(instancia)