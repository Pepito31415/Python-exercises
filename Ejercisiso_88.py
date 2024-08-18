#Realiizar un algoritmo que introduzca un nuevon eelemento en un vector ordenado ascendentemente 
#el vector debe conservar el orden.

print("-----------------------------------------------")
print("INGRESAR VALOR EN EL VECTOR ASCENDENTE.")
print("-----------------------------------------------")

v=[]

print("ingrese los 10 valores del vector")
for i in range(10):
    valor=int(input("valor {}: ".format(i+1)))
    v.append(valor)

valor11= int(input("Ingrese el valor a inserttar: "))
v.append(valor11)

#proceso
#ordenar vector
for x in range(11):
    for y in range(10):
        if v[y]>v[x]:
            a=v[y]
            v[y]=v[x]
            v[x]=a

for x in range(11):
    print(v[x])