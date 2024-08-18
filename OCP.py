#Ejercisio de principio de ocp

class notificador:
    def __init__(self, usuario, mensaje):
        self.usuario=usuario
        self.mensaje=mensaje

    def notificar(self):
        raise NotImplementedError


class NotificadorEmail(notificador):
    def notificador(self):
        print(f"EWnviando mensaje por EMAIL a {self.usuario.email}")

class NotificadorSMS(notificador):
    def notificar(self):
        print(f"Enviando SMS a {self.usuario.sms}")

class NotificadorWsa(notificador):
    def notificar(self):
        print(f"Enviando un wasa a {self.usuario.wasa}")        