#Ejercisio 111: crear un juego interactivo donde los personajes peleen entre si, tengan fuerza, resistencia,
# velocidad(funcion que defina los turnos), y estos puedan fucionarse entre si, y que al comenzar el juego el
# usuario decida con que personaje empezar y si quiere modo de 
# juego de estos fucionados.

print("---------------------------------------------------------------")
print("JUego en EJECUCION")
print("---------------------------------------------------------------")



e_p=int(input("\n Elige tu personaje:__ "))



class Personaje:
    def __init__(self, nombre, fuerza, velocidad,resistencia):
        self.nombre=nombre
        self.fuerza=fuerza
        self.velocidad= velocidad
        self.resistencia=resistencia

    def __repr__(self):
        return f"{self.nombre} (fuerza: {self.fuerza}, velocidad: {self.velocidad}, {self.resistencia})"
    
    def __add__(self,otro_pj):
        nuevo_nombre= self.nombre+"-"+ otro_pj.nombre
        nueva_fuerza= round(((self.fuerza+otro_pj.fuerza)/2)**1.34)
        nueva_velocidad= round(((self.velocidad+otro_pj.velocidad)/2)**1.34)
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)

class F_pelea(Personaje):
    def __init__(self, nombre, fuerza, velocidad, resistencia):
        super().__init__(nombre, fuerza, velocidad, resistencia)
        if fuerza<resistencia:
            print(f"Tu personaje {self.nombre} es mas debil")
        else:
            print("tu personaje: {self.nombre} es mas fuerte")
            if fuerza>resistencia and velocidad>fuerza:
                print("Has ganado")
            else:
                return "Tu personaje ha perdido"
            
goku=Personaje("Goku",30,20,100)
vegeta=Personaje("Vegeta",25,33,100)
krilin=Personaje("Krilin",10,25,60)
frezeer=Personaje("Frezeer",80,40,350)


while e_p!=1 and e_p!=2 and e_p!=3 and e_p!=4:
    print("EL NUMERO DE PERSONAJE NO EXISTE, ingrese un numero existente")
    e_p=int(input("\n Elige tu personaje:__ "))
    if e_p==2:    
        vegeta=Personaje("Vegeta",25,33,100)
        e_p=vegeta
        print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
        print(f"Has elegido a {e_p.nombre} que su fuerza es de {e_p.fuerza} y resistencia es de {e_p.resistencia} y velocidad de {e_p.velocidad}")
        break
    elif e_p== 3:
        krilin=Personaje("Krilin",10,25,60)
        e_p=krilin
        print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
        print(f"Has elegido a {e_p.nombre} que su fuerza es de {e_p.fuerza} y resistencia es de {e_p.resistencia} y velocidad de {e_p.velocidad}")
        break
    elif e_p== 4:
        frezeer=Personaje("Frezeer",80,40,350)
        e_p=frezeer
        print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
        print(f"Has elegido a {e_p.nombre} que su fuerza es de {e_p.fuerza} y resistencia es de {e_p.resistencia} y velocidad de {e_p.velocidad}")
        break
    elif e_p==1:
        goku=Personaje("Goku",30,20,100)
        e_p=goku
        print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
        print(f"Has elegido a {e_p.nombre} que su fuerza es de {e_p.fuerza} y resistencia es de {e_p.resistencia} y velocidad de {e_p.velocidad}")
        break