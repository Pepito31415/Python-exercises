#Ejercisio 118: Principio de abierto cerrado (OCP):
# -Disseña un sistema de envio de notificaciones, Crea una clase base "Notificacion" con metodos como
# "sennd()" 
# -Extiende esta clase con clases como "EmailNotification" y "SMSNotification" sin modificar el codigo original.

class Notification:
    usuario=input("Ingrese usuario:_ ")
    print("-----------------------------------")
    mensaje=input("escribe un mensaje:_ ")

    def __init__(self, usuario, mensaje):
        self.usuario=usuario
        self.mensaje=mensaje
    
    def send(self):
        print(f"... Enviando mensaje a {self.usuario}")
        return f"Mensaje: {self.mensaje} enviado a {self.usuario}"
    
class EmailNotfication(Notification):
    def send(self):
        print(f"... Enviando email a {self.usuario}")
        return f"Email: {self.mensaje} enviado a {self.usuario}"
    
class WhasappNotfication(Notification):
    def send(self):
        print(f"... Enviando wasa a {self.usuario}")
        return f"Wasa: {self.mensaje} enviado a {self.usuario}"
    
notification=Notification
email=EmailNotfication
wasa=WhasappNotfication

email.send(notification)
wasa.send(notification)