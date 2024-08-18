#Eleaborar un algoritmo que ordfene descendentemente un vector.

print("-------------------------------------------------")
print("ORDENAR DECENDENTEMENTE EL VECTOR.")
print("-------------------------------------------------")

#inicializar
V1=[]

#entrada
n=int(input("Ingrese los valores del vector: "))
for x in range(n):
    valor=int(input("V{}: ".format(x+1)))
    V1.append(valor)

#proceso
print("los elementos del vector son:_ ")
for y in range(n):

    for x in range(n-1):
        if V1[x]<V1[x+1]:
            m=V1[x+1]
            V1[x+1]=m

print(V1)