#Ejercisio 82: determinar el orrden de los bytes en la arquitectura de ejecucion actual.

import sys

if sys.byteorder == 'little':
    print("plataforma little-endian")
else:
    print('Plataforma big endian')    