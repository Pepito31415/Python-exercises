#Ejercisio 115: Principio de segregacion de interfaz(ISP): 
# diesña una interfaz "Worker" con metodos como "work()" y "get_salary()".
# implementa clases como "Developer", "Manager", y "Desingner" que
# se adhieran a la interfaz adecuadamente.

from abc import ABC, abstractclassmethod

class Worker:
    def __init__(self, profecion, salario):
        self.profecion=profecion
        self.salario=salario

    @abstractclassmethod
    def work(self):
        print(f"el {self.profecion} esta trabajando")
    @abstractclassmethod
    def get_salary(self):
        print(f"Recoger el salario de {self.salario}")
    
class Developper(Worker):
    profecion="Programador"
    salario="2000"

class Manager(Worker):
    profecion="representante"

class Desingner(Worker):
    profecion="diseñador"
    salario="1500"

worked=Worker
developper=Developper
manager=Manager
desingner=Desingner

developper.work()
developper.get_salary()
desingner.work()
desingner.get_salary()
manager.work()