#Ejercisio 138: generador de contraseñas usando funciones anidadas:

import random
import string

def generar_contraseña(longitud):
    def seleccionar_caracter():
        return random.choice(string.ascii_letters+ string.digits+string.punctuation)
    
    contraseña= " ".join(seleccionar_caracter() for _ in range(longitud))
    return contraseña

print(generar_contraseña(12))