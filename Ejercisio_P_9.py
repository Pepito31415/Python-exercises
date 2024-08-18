#Crear un algoritmo, que dado N numeros enteros ingresados por teclado determine cual de ellos es el menor y es el mayor respectivamente.

#Decoracion del programa

print("------------------------------------------------------")
print("Ingrese la cantidad de numeros a evaluar:___ ")
print("------------------------------------------------------")

#proceso y lectura de datos

lim = int(input())

print("------------------------------------------------------")
print("Ingrese los numeros:__ ")
print("------------------------------------------------------")

n=int(input())

men=n
may=n

#uso del bucle for

for i in range(1, lim): #USo repectivo de la cantidad impuesta por el usuario determinada por la funcion for.
    n=int(input("Ingrese numeros:__ "))

    if n< men:
        men=n
    else:
        if n> may:
            may=n

#Salida

print("\nSalida:__")
print("------------------------------------------------------")
print("El numero menor es:__", men)
print("El numero mayor es:__", may)
print("------------------------------------------------------")