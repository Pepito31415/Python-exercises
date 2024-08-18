#Notacion 35: Elimnar archivos usando python.

import os
import shutil

path="C:\\Users\\jesus\\OneDrive\\Documentos\\codigos de practica de Angel\\Phyton\\ejercisios\\folder"

try:
   # os.remove("C:\\Users\\jesus\\OneDrive\\Documentos\\codigos de practica de Angel\\Phyton\\ejercisios\\folder")
   #os.rmdir(path)
   shutil.rmtree(path)
except FileNotFoundError:
    print("El archivo no se encontro")
except PermissionError:
    print("lo siento, no tienes permiso para eliminar esta carpeta")
except OSError:
    print("no puedes eliminar eso usando esa funcion.")
else:
    print(path,"Fue eliminado")