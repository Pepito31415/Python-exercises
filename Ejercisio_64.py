#Ejercisio 64: consultar la fev¿cha de creaciom y de modificacioon de un archivo.

import os.path, time

nombre_archivo= 'archivo.txt'

print('Fecha creacion: {}'.format(time.ctime(os.path.getctime(nombre_archivo))))

print('Fecha de modificacion: {}'.format(time.ctime(os.path.getmtime(nombre_archivo))))