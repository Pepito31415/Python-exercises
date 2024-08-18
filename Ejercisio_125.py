#Ejercisio 125: Filtarar numeros por medio de la funcion filter.

numeros=[i for i in range(10)]

print(numeros)

filtro_omares= lambda x: x%2==1

impares =filter(filtro_omares, numeros)

print(list(impares))