#Ejercisio 126: obtener el numero de ID de un objeto.

numeros=[2,3,5]

print(id(numeros))
print(id(numeros))
print(id(numeros))
print(id(numeros))
print(id(numeros))

def mostrar_id(objeto):
    print(id(objeto))
    
mostrar_id(numeros)

objeto= object()

mostrar_id(object)