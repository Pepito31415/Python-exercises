#3Nootaaccion 25: args en python.

def suma(*args):
    suma=0
    cosas=list(args)
    cosas[1]=0
    for i in cosas:
        suma+=i 
    return suma
    
print(suma(1,5, 3,2, 7, 1))