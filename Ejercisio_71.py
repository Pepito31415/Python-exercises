#Ejercisio 71: Calcular el tamaño de un archivo.

import os

archivo = r'C:\Users\jesus\OneDrive\Documentos\codigos de practica de Angel\Phyton\ejercisios'

def calcular_tamagmio_archivo(archivo):
    """
    calcula el tamaño del archivo en bytes.
    """
    try:
        return os.path.getsize(archivo)
    except:
        return None
    
print(calcular_tamagmio_archivo(archivo))    

archivo = r'C:\Users\jesus\OneDrive\Documentos\codigos de practica de Angel\Phyton\ejercisios.ph'

print(calcular_tamagmio_archivo(archivo))