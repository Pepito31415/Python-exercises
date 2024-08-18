#Notacin 14: metodos especiales o metodos dunder.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre= nombre
        self.edad=edad

    def __str__(self):
        return f"persona( {self.nombre},edad={self.edad})"
    
    def __rep__(self):
        return f'persona( "{self.nombre}",{self.edad})'

    def __add__(self,otro): #El metodo eswpecial __add__ permite crar o concatenar con diferentes procesos valores de objetos de clases con mismos
                            #atributos de clases de herncia o abstractas  
        nuevo_valor= self.edad+ otro.edad
        return Persona(self.nombre+otro.nombre,nuevo_valor)

dalto= Persona("lucas",21)
pedro= Persona("Pedro",30)
maria= Persona("Maria",18)

nueva_persona= dalto + pedro + maria
print(nueva_persona.nombre)
print(nueva_persona.edad)

#este codigo es la prueva de que cualquier clase sin importas la
# diferenca de de atributos y sus funciones... estas se pueden concatenar.  