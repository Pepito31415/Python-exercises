#Ejercisio 165: Listar archivos en un directorio

import os
dir_path='C:\\Users\\jesus\\OneDrive\\Documentos\\codigos de practica de Angel\\Phyton\\ejercisios'
files=os.listdir(dir_path)
print(f"Archivos en el directorio: {files}")