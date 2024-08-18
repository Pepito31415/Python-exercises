#Ejercisio 49: mortrar los archivos de un directorio epecifico

from os import listdir
from os.path import isfile, join

ruta= r'C:\Users\jesus\OneDrive\Documentos\codigos de practica de Angel\Phyton\ejercisios'

def listar_directorio(ruta):
    """
    Lista el contenido de archivos de un directorio especifico.
    """
    archivos=[a for a in listdir(ruta) if isfile(join(ruta, a))]

    return archivos

listado_archivos= listar_directorio(ruta)

print(listado_archivos)