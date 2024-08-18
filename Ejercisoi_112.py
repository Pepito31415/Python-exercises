#Ejercisio 112: Crear una clase "File Reader" que lea datos de un archivo y una clase "Dataprocessor" que procese esos datos. 
# Ambas clases deben tener una unica responsabilidad 
# -Asegurarse de que las clases no mezclen la lectura de archivos con el procesamiento de datos.

#Este ejercisio aplica lo visto en la notacion 15, el principio de responsabilidad unica 

class ReadFile:
    def read(self):
        return "archivo leido" #creando la clase que hipoteticamente leera el archivo 

class DataProsessor(): #creando la clase que hipoteticamente va procesar el archivo ya leido
    def __init__(self, reading):
        self.reading=reading
    def procesado(self):
        print(reading.read())
        return "archivo procesado"

reading=ReadFile() #asignando la funcion de la clase a algo mas practico de ejecutar
procesador=DataProsessor(reading) #asignando la clase del procesador a algo mas practico deejecutar
                                  #mientras se le asigna la funcion dependiente de esta indirectamente
print(procesador.procesado())

#aprendi con esto a no dar tantas vueltas y buscar una solucion practica pero no vaga.