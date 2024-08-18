#Cargar un vector de 100 pocisiones con numero enteros, a partir de este crear 2 vectores; 
# uno con pares y e otro con los numeros impares, ademas decir de los vectores cueal
# es el mas grande y el numero de elemntos es cada vector
# inicialmente los vectores estaran limpios, esto quiere decir que todas las posiciones tendran el valor 0(cero).

print("----------------------------------")
print("SEPARAR PARES E IMPARES.")
print("----------------------------------")

#INICIALIZAR
vec=[]

#Entradas
print("Ingrese dimension del vector: ")
tam_vec=int(input())

pares=tam_vec*[0]
impares=tam_vec*[0]

print("Ingrese los ",tam_vec," valores del vector:__ ")
for x in range(tam_vec):
    elemento=int(input("Elemento{}: ".format(x+1)))
    vec.append(elemento)

vpr=0
i=0
for x in range(tam_vec):
    if vec[x]%2==0:
        pares[vpr]=vec[x]
        vpr=vpr+1
    else:
        impares[i]=vec[x]
        i=i+1

print(pares[0:vpr])
print("El vector de pares tiene",vpr,"elementos")
print("----------------------------------")
print(impares[0:i])
print("El vector de impares tiene",i,"elementos")

if vpr>i:
    print("El vector de pares es al mas grande")

elif vpr<i:
    print("El vector de impares es el mas grande")

else:
    print("Los 2 los vectores son iguales en un numero de elementos")