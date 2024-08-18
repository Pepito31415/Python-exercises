#Ejercisio 144: Registro de eventos.

eventos=[]

def registrar_evento(**kwargs):
    eventos.append(kwargs)
    
registrar_evento(tipo="error", mensaje="Archivo no encontrado", codigo=404)
registrar_evento(tipo="Advertencia", mensaje="espacio del disco bajo")
print(eventos)