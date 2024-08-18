#creando mi propia excepcion personalisada
class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"Impresionante, cometiste el siguiente error: {err}")
        
try:#lanzando mi propia excepcion #su manejo
    raise MiExcepcion("Jajajajajajajajaja, cometiste poco culto")
except:
    print("Poco vas a cometer ese error")