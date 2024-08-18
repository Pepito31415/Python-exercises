#Ejercisio 58: Calcular la suma de los primeros n numeros enteros:

#Usando la foremula de Gaus: n*(n+1)/2

n=10

suma= n*(n+1)/2

print(suma)

print()

#usando un cclo
suma=0

for i in range(1, n+1):
    suma+= i

print(suma)    

print()

#Usando la funcion sum:

suma= sum(range(1,n+1))

print(suma)