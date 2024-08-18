#Ejercisio 39: calcular el valor futro parar una cantidad, interes, y numero de años espesificos.

def valor_futuro(vp,i,n):
    """
    Calcular el valor Futuro.
    """
    return vp*(1+i)**n


valor_presente=10000
interes=3.5
periodos=7

print(valor_futuro(valor_presente,interes/100,periodos))