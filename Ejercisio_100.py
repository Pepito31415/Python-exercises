#Ejercisio 100: Obtener el tamaño de un archivo.

ruta= r'C:\Users\jesus\OneDrive\Documentos\codigos de practica de Angel\estructura_SD.psc'

import os

archivo_bytes=os.path.getsize(ruta)

print(archivo_bytes)