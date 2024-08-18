#3Ejercisio 132: Ffiltrar numeror pares.

#dada de una lista dada de  nnumeero, solo ffiltrra los pares.

numeros=[1,2,3,4,5,343,56,9823]

def es_par(num):
    return num%2==0

numeros_pares=list(filter(es_par, numeros))
print(numeros_pares)