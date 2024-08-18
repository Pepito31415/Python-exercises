#Ejercisiso 116: Principio de invercion de dependencias(DIP)
# crea una clase "Database" que maneje la conexion a una base de datos.
# luego, crea una clase "UserService" que dependa de "Databaes" a travez 
# de una abstraccion(por ejemplo, una clase base)  

from abc import ABC, abstractclassmethod

class Database(ABC):
    @abstractclassmethod
    def datos(self):
        print("leido los datos")

class UserService:
    def __init__(self, datos):
        self.datos=datos
    def procesador(self,datos):
        if datos==datos:
            print("-----------------------------")
            print("PROCESADO")
            return "----------------------"
datos=Database
procesador=UserService(datos)
+procesador=UserService(datos.datos())
procesador=UserService(procesador.procesador(datos))
