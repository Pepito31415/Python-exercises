#Ejercisio 32: Calcular la suma de tres numeros si todos son diferentes, en caso de ser lo contrario la suma sera de 0

def sumar (x,y,z):
    """
    suma tres numeros. Si los tres numeros son iguales, la suma sera 0. 
    """
    if x== y or x==z or y==z:
        return 0
    else:
        return x+y+z
    
print(sumar(2,5,3))
print(sumar(2,5,2))
print(sumar(5,5,2))    
print(sumar(11,7,5))
