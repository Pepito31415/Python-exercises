#ejescisio 63: Comprobar si el nombre de un archivo correspomde con una ruta absoluta.


from os import path

nombre_archivo= 'archivo.txt'
nombre_archivo_2= r'C:\Users\jesus\OneDrive\Documentos\codigos de practica de Angel\Phyton\ejercisios'

print(path.isabs(nombre_archivo))
print(path.isabs(nombre_archivo_2))
print(__file__)
print(path.isabs(__file__))