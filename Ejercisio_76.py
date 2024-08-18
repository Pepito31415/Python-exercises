#Ejercisio 76: Obtener los argumentos de lineas de comandos.

# $ python programa.py 1 python

import sys

nombre_script = sys.argv[0]
cantidad_args= len(sys.argv)
argumentos= str(sys.argv)

print('Nombre script: {}'.format(nombre_script))
print('Cantidad de argumentos {}'.format(cantidad_args))
print('Lista de argumentos: {}'.format(argumentos))

