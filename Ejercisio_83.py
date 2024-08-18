#Escribir un algoritmo que pida un vector de caracteres por
#pantalla e invierrta el orden de los caracteres mostrandolo por pantalla.
#La inversion se hara sin utilizar otro vector auxiliar.

#decoracion
print("-------------------------------------------------")
print("INVERTIR CARACTERES DE UN VECTOR")
print("-------------------------------------------------")

#entradas
n=int(input("ingrese dimension del vector:_ "))

v=n*['']

for i in range(n):
    v[i]=input("ingrese Caraccter: ")

#proceso
z=''
d=n
for i in range(n//2):
    z=v[i]
    v[i]=v[d-1]
    d=d-1

#sallida
for i in range(n):
    print(v[i])
    