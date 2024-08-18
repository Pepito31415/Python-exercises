#Esccribir un algoritmo qeu calcule el producto a cancelar
# y vectorial de dos vectores de 3 elements cuyos valores se introducen por pantalla.

print("---------------------------------------------")
print("Producto vectorial y escala")
print("---------------------------------------------")

V1=3*[0]
V2=[0]*3

#Entradas

for i in range(3):
    V2[i]= int(input("V2({}):".format(i+1)))

#proceso
sum=0

for i in range(3):
    P=V1[i]*V2[i]
    sum=sum+P

print("El producto escalar es:",sum)
x=V1[1]*V2[2]-V1[2]*V2[1]
y=-(V1[0]*V2[2]-V1[2]*V2[0])
z=V1[0]*V2[2]-V1[2]*V2[0]
print("El producto vectorial es: {}i {}j {}k".format(x,y,z))