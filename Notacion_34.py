#Notacion 34: Moviendo archivos en python.

import os

origen= 'C:\\Users\\jesus\\OneDrive\\Documentos\\documetos de blender de angel\\archivo.txt'
destino='C:\\Users\\jesus\\OneDrive\\Documentos\\codigos de practica de Angel\\archivo.txt'

try:
    if os.path.exists(destino):
        print("ya hay un archivo en este destino")
    else:
        os.replace(origen, destino)
        print(origen+"fue movido")
except FileNotFoundError:
    print(origen, "No fue encontrado")
    