#Ejercisio 45: ejecutar un comando externo por medio de la funcion sell.

from subprocess import call #importacion del modulo para la creacion del programa.

print(call(["ping","google.com"])) #en resumen este comando detecta a cuanto de ping esta un sitio web o un servidor o cualquier cosa conectada a nternet.
