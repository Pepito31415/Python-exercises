#Ejerciso 46:encontrar la ruta del script actual en ejecucion.

import os #importacion del modulo.
#detecta desde donde se ejecuta el programa
print(os.path.realpath(__file__)) #salida del comando