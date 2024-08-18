#Ejercisio 117: Principio de responsabilidad Unica(SRP):
# -Crea una clase "logger" que maneje el registro de eventos en una aplicacion.
# -LUego, implementa una clase "User" que se encargue de la autenticacion y autorizacion.

class Loger:
    def review_frist():
        print("------------------------------------------")
        print("revisando eventos de las aplicaciones")
        return "------------------------------------------"
    
class User():
    def __init__(self, loger):
        self.loger=loger

    def authentication(self):
        print("------------------------------------")
        print("todo esta autenticado, esta autorizado todo para usar")
        print("------------------------------------------------")
        return "TODO ESTA AUTORIZADO PARA SU USO"
    
loger=Loger
user=User(loger)

print(loger.review_frist())
print(user.authentication())