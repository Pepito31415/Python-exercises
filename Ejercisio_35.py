#Ejercisio 35: Crear una  funcion unicamente para sumar numeros enteros.

def sumar(x,y):
    """
    Su,a dos numeros. Valida que estos numeros sean enteros.
    """
    if isinstance(x, int) and isinstance(y, int):
        return x+y
    else:
        raise TypeError("los valores deben de ser enteros.")
    
try:
    print(sumar(2,3))
    print(sumar(2,"3"))
except TypeError as e:
    print(e)        