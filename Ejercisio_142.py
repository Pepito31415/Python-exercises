#Ejercisio 142: informacion del usuario.

def mostrar_informacion(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
        
mostrar_informacion(nombre= "juan", edad= 32, ciudad= "Bogota")