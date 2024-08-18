#Ejercisio 128: Comprobar si una cadena de caracteres representa un numero.

def es_numero(cadena):
    try:
        float(cadena)
        return True
    except (TypeError, ValueError):
        return False
    
cadena= "2.7182"
print(es_numero(cadena))

cadena= "2.7182abc"
print(es_numero(cadena))

cadena= (5.3, 7.9)
print(es_numero(cadena))