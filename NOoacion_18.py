#Notacion 18: principio de segregacion de interfas.

#ISP

from abc import ABC, abstractclassmethod

# class Trabajador(ABC):

#     @abstractclassmethod
#     def comer(self):
#         pass

#     @abstractclassmethod
#     def trabajar(self):
#         pass
    
#     @abstractclassmethod
#     def dormir(self):
#         pass

# class Humano(Trabajador):
#     def comer(self):
#         print("El humano esta comiendo")

#     def trabajar(self):
#         print("El humano esta trabajando")

#     def dormir(self):
#         print("El humano esta durmiendo")

# class Robot(Trabajador):
#     def trabajar(self):
#         print("El humano esta trabajando") ------------>#en casos como ests
#                                                         #estamos violando el principio
#                                                         #de segregacion de interfas.
# robot=Robot()

class Trabajador(ABC):
    @abstractclassmethod
    def trabajar(self):
        pass

class Comer(ABC):
    @abstractclassmethod
    def comer(self):
        pass

class Durmiente(ABC):
    @abstractclassmethod
    def dormir(self):
        pass

class Humano(Trabajador, Durmiente, Comer):
    def comer(self):
        print("El humano esta comiendo")

    def trabajar(self):
        print("El humano esta trabajando")

    def dormir(self):
        print("El humano esta durmiendo")

class Robot(Trabajador):
    def trabajar(self):
        print("El robot esta trabajando")

robot=Robot()
humano=Humano()

robot.trabajar()
humano.trabajar()
humano.comer()

#esta es la forma mas factible para cumplir el principio de segregacion de interfaz.