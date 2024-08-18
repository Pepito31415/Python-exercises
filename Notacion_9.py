
# def saludo():
#     print("hola mundo")

# saludo_modificado=decorador(saludo)
# saludo_modificado()

#Esto es un ejemplo perfecto de una funcion decoradora, agrega una funcion antes y despues.


def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a la funcion")
        funcion()
    return funcion_modificada

@decorador
def saludo():
    print("hola dalto como andas")

saludo()