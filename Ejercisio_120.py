#Ejercisio 120: principio de segregacion de interfaz (ISP):
#-Diseña una interfaz "Paymentgateway" con metodos como "process_pay" y "refund()"
# -Implementa clases como "creditCardGateway" y "PayPalGateway" que se adhieran a la 
# interfaz adecuadamente.

from abc import ABC, abstractmethod

class Paymentgateway(ABC):
    pay=int(input("Ingrese cantidad de fondos:__ "))
    def __init__(self,pay):
        self.pay=pay
    @abstractmethod
    def process_pay(self):
        print(f"pagando {self.pay}")
    @abstractmethod
    def refound(self):
        print(f"Rembolsando {self.pay}")

class CreditCardGateway(Paymentgateway):
    def process_pay(self):
        print(f"pagando {self.pay}")
    def refound(self):
        print(f"Rembolsando {self.pay}")

class PaypalGateway(Paymentgateway):
    def process_pay(self):
        print(f"pagando {self.pay}")
    def refound(self):
        print(f"Rembolsando {self.pay}")



credito=CreditCardGateway
pays=Paymentgateway
paypal=PaypalGateway

credito.process_pay(pays)
credito.refound(pays)
print("---------------------------------------------")
paypal.process_pay(pays)
paypal.refound(pays)