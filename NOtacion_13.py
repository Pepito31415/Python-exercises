#Notacion 113: clases abstractas

from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod  #las clases abstractas son como una especie de plantilla para la clases
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
        self.actividad=actividad

    @abstractclassmethod
    def hacer_actividad(self):
        pass

    def presentacion(self):
        print(f"Hola, me llamo: {self.nombre} y tengo {self.edad} años")
#al final se pueden crear diferentes tipos de funciones para una clase abstracta
# esto con el fin de crear cierto pilimorfismo para volver el codigo una ehrramienta de uso mas practico

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
        
    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")

class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
        
    def hacer_actividad(self):
        print(f"Actualmente estoy trabajando en el rubro de programacion: {self.actividad}")

pedrito=Estudiante("Pedrito",25,"no binario","Programacion")
dalto=Trabajador("lucas",21,"masculino","Programacion")

dalto.presentacion()
dalto.hacer_actividad()
pedrito.presentacion()
pedrito.hacer_actividad()