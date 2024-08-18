#Notacion 30:pr4actica de deteccion de archivos

import os

path='C:\\Users\\jesus\\OneDrive\\Documentos\\codigos de practica de Angel\\Phyton\ejercisios\\archivo.txt'
path='C:\\Users\\jesus\\OneDrive\\Documentos\\codigos de practica de Angel\\Phyton\ejercisios'

if os.path.exists(path):
    print("la ubicacio existe")
    if os.path.isfile(path):
        print("es un archivo!")
    elif os.path.isdir(path):
        print("Es un directorio!")
else:
    print("esta ubicacion no existe")