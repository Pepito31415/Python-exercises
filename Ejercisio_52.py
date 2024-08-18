#Ejercisio 52: Imprimir en la salida estandar de errores.

import sys

#print('Este es un error',file=sys.stderr)

def eprint(*args,**kwargs):
    print(*args,file=sys.stderr)

eprint('esto es un mensaje de error')    