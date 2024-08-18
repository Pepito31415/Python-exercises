#Ejercisio N 36: Crear una clase para representar los datos de una persona


class Persona:
    def __init__(self,nombre,edad,correo):
        self.nombre=nombre
        self.edad=edad
        self.correo=correo

    def __str__(self):
        return "nombre: {}\nEdad {}\nCorreo {}".format(self.nombre,self.edad,self.correo)
    
Edward = Persona("edward","33","Edward@gmail.com")

print(Edward)