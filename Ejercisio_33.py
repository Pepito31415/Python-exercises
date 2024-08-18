#Ejercisio 33: Sumar dos numeros. Si la suma esta entre 10 y 30, retornar 30.

def sumar(x,y):
    """
    suma dos numeros. Si la suma se halla entre 10 y 30, se retorna 30.
        """
    suma=x+y

    if suma in range(10,30+1):
        return 30
    else:
        return suma
    
print(sumar(7,3))
print(sumar(7,23))
print(sumar(12,17))
print(sumar(23,17))
