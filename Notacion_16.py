#Notacion 16: OCP principio de abierto y cerrado.

class Notificador:
    def __init__(self,usuario, mensaje):
        self.usuario=usuario
        self.mensaje=mensaje
    
    def notificar(self):
        raise NotImplementedError
    
class notificadorEmail(Notificador):
    def Notificador(self):
        print(f"enviando mensaje por mail a {self.usuario.email}")

class notificadorEmail(Notificador):
    def Notificador(self):
        print(f"enviando mensaje por sms a {self.usuario.sms}")

class notificadorWhatsApp(Notificador):
    def Notificador(self):
        print(f"enviando mensaje por whatsapp a {self.usuario.whatsapp}")

#este principio consiste que si el usuario creador del codigo sabe que el programa va serr modificado o
# actulizado en el futuro; lo mejor seria dejar un codigo abierto para que este pueda tener mas funciones sin este ser modificado directamente
# cumpliendo a su vez tambien el principio de responsabilidad unica.

class notificadorTwiter(Notificador):
    def Notificador(self):
        print(f"enviando mensaje por twiter a {self.usuario.twiter}")