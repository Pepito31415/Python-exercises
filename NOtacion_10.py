#Notacion 10: decoradores y sus tipos y funciones.

def funcion_decoradora(funcion_parametro):
    def funcion_interior():
        #Acciones adicionales que decoran
        print("Vamos a realizar un calculo: ")
        funcion_parametro()
        #Mas accionse que decoran.
        print("Hemos terminado el calculo")
    return funcion_interior

@funcion_decoradora
def suma():
    print(15+20)

@funcion_decoradora
def resta():
    print(20-10)

suma()
resta()