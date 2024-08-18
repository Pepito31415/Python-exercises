#ejercisio 98: determinar si una ruta es correspondiente a un archivo o carpeta.

import os

def validar_ruta(ruta):
    if os.path.isdir(ruta):
        return 'Es un directorio'
    elif os.path.isfile(ruta):
        return 'Es un archivo'
    else:
        return 'Es un archivo especial (socket, dispositivo de gestion archivos)'
    
ruta= r'C:\Users\jesus\OneDrive\Documentos\codigos de practica de Angel'

print(validar_ruta(ruta))