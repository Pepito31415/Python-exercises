#Ingresar 50 caracteres para ver cuantas veces se repite "a".

#inicio

#datos
ca=0
num_car=10

#decoracion
print("-----------------------------------------------------------")
print("Ingrese",num_car ,"caracteres en del orden que usted desee:__ ")
print("-----------------------------------------------------------")


for i in range(0,num_car): #proceso del bucle for
    m=input("Ingrese caracter:__ ")
    if m=="a":
        ca=ca+1

#este codigo reconoce el mprimer caracter puesto en cualquiera de las 10 entradas.

#salida

print("-----------------------------------------------------------")
print("\nSalida")
print("-----------------------------------------------------------")
print("En ",num_car,"caracteres hay",ca,"caracteres: A.") #Resultado de la salida.
print("-----------------------------------------------------------")