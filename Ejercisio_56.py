#Ejercisio 56: Obtener eñ tamaño de la  ventana del terminal.

import fcntl, termios, struct

def calcular_tamagnio_terminal():
    th, tw,hp, wp=struct.unpack('HHH',fcntl.ioctl(0, termios.TIOCGWINSZ, struct.pack('HHH',0,0,0,0)))

    return tw, th

print(calcular_tamagnio_terminal())#paquete Fcntl no intalado.