#Ejercisio 163: obtener informacion sobre archivos y directorios.

import os 

file_path= 'C:\\Users\\jesus\\OneDrive\\Documentos\\codigos de practica de Angel\\Phyton\\ejercisios\\copy(archivo).txt'
stats=os.stat(file_path)
print(f'tamaño del archivo:{stats.st_size} bytes')