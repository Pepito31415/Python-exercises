##jercisio 96: Comprobar si todos los elementos de una coleccion son mayores respecto a un nummero.

numeros=[7,3,2,5,11]

print(all(x>1 for x in numeros))
print(all(x>5 for x in numeros))