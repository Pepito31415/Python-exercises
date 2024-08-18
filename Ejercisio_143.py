#Ejercisio 143: configuracion de parametros usando kwargs.

def configurar_aplicacion(**kwargs):
    configuracion={
        "resolucion": "1920x1080",
        "volumen": 50,
        "brillo": 70
    }
    configuracion.update(kwargs)
    return configuracion

nueva_configuracion= configurar_aplicacion(volumen=80, brillo=90)
print(nueva_configuracion)