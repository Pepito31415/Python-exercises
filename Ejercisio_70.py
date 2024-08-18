#Ejercisio 70: Ordenar un conjunto dde archivos por fecha de creacion.

import glob
import os

ruta= r'C:\Users\jesus\OneDrive\Documentos\codigos de practica de Angel\Phyton\ejercisios'

archivos = glob.glob(ruta + os.path.sep +'*.py')

archivos.sort(key=os.path.getctime)

print('\n'.join(archivos))