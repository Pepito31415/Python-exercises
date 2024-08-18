#Ejercisio 136: suma de numeros.

def operacion(a, b, c):
    def suma(x,y):
        return x+y
    
    resultado_suma=suma(a, b)
    return resultado_suma*c

print(operacion(4,3,2))