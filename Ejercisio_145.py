#Ejercisio 145: registro de eventos usando los modulos args y kwargs.

eventos=[]

def registrar_eventos(*args, **kwagrs):
    evento= {
        "descripcion": args,
        "detalles": kwagrs
    }
    eventos.append(evento)
    
registrar_eventos("Error de sistema", codigo= 500, mensaje= "Error interno del servidor")
registrar_eventos("Advertencia", codigo= 300, mensaje= "espacio del disco bajo")
print(eventos)