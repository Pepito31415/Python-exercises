#corrector ortografico

# class Diccionario:
#     def verificar_palabra(self, palabra):
#         #logica para verificar palabra
#         pass

# class CorrectorOrtografico:
#     def __init__ (self):
#         self.diccionario= Diccionario()

#     def corregir_texto(self, texto):
#         #usando el diccionario para corregir el texto
#         pass

from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificator_palabra(self, palabra):
        # logica para verificar palabras
        pass

class Diccionario(VerificadorOrtografico):
    def verificator_palabra(self, palabra):
        #logica para verificar palabras si esta en el diccionario
        pass

class ServicioOnline(VerificadorOrtografico):
    def verificator_palabra(self, palabra):
        #logica para verificar palabras
        pass

class CorrectorOrtografico:
    def __init__(self, verificardor):
        self.verificador= verificardor

    def corregir_texto(self, texto):
        #usamos el verificador para corregir texto.
        self.texto= texto

corrector= CorrectorOrtografico(Diccionario())