#Notacion 31: como leer el contenido de un archivo.
try:
    with open('C:\\Users\\jesus\\OneDrive\\Documentos\\codigos de practica de Angel\\Phyton\ejercisios\\archivo.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("el archivo no fue encntrado")