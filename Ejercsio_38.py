#Ejercisio 38:Resolver la expocision algebraica (x+y)*(x+y)-

#(x+y)*(x+y)=x´**2+2xy+y**2
#(2+3)*(2+3)=5*5=25

def evaluear_expresion(x,y):
    """
    Resuelve ñla exprecion algebraica (x+y)*(x+y).
    """
    return x**2+2*x*y+y**2  #procedimento de la evaluacion.


x=float(input("escribe el valor de x: ")) #Leyendo los datos que ingresa el usuario
y=float(input("escribe el valor de y: "))

print(evaluear_expresion(x,y)) #Salida del codigo.
