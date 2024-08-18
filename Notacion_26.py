#Notacion 26: *kwargs.

def hola(**kwargs):
   print("hola", end=" ")
   for clave, valor in kwargs.items():
       print(valor, end= " ")
       
hola( señor="señor" ,nombre="Angel", apellido="Smith", segundo_nombre= "python")