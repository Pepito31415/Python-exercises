#Ejercisio 121: principio de inversion de dependencias (DIP):
#Crea una clase "NotificationService" que envie notificaciones a travez de una abstracion (por ejemplo, una interfaz
# o clase base)
# -Luego implemeta clases como "EmailService" y"SMSService" que dependan de esta abstracion.

from abc import ABC, abstractmethod

class Notificatio(ABC):
    @abstractmethod
    def send():
        medio=medio
        print(f"enviar mensaje por {medio}")

class EmailService(Notificatio):
    def send():
        medio="Email"
        print(f"enviar mensaje por {medio}")

class SMSService(Notificatio):
    def send():
        medio="SMS"
        print(f"enviar mensaje por {medio}")

sms=SMSService
email=EmailService
email.send()
sms.send()