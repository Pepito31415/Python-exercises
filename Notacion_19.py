#Notacion 19: principio de invercion de dependencia.

#ISP

# class Diccionario:
#     def verificar_palabra(self, palabra):
#         #logica para verificar palabras
#         pass

# class CorrecorOrtografico:
#     def __init__(self):
#         self.diccionario= Diccionario()

#     def corregir_texto(self, texto):
#         #usamos el diccionario para corregir el texto
#         pass --------------------------------------------------->el principio de invercion de dependencia, una funcion o 
                                                                 #o clase no puede depender completamente de otra clase.

from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra):
        pass

class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        #logica para indentificar palabras si esta en el diccionario
        pass

class CorrectorOrtografico:
    def __init__(self,verificador):
        self.verificador=verificador

    def corregir_texto(self, texto):
        self.texto=texto
        #usamos el verificador para corregir texto.

corrector= CorrectorOrtografico(Diccionario())