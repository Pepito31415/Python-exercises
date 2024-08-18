#Elaborar algoritmo que busque la forma secuencial un
#VALOR dentro de un arreglo de N elemntos numericos y 
#retome su pocision.

print("-------------------------------------------------")
print("BUSCAR ELEMENTO DENTRO DEL ARRAY.")
print("-------------------------------------------------")

valor=[]

#entradas
m=int(input("Ingrese numero de elementos del areglo: "))
print("-------------------------------------------------")
print("ingrese elementos del arreglo:_ ")
for i in range(m):
    elemento=int(input("Ingrese Elemnto._"))
    valor.append(elemento)

#Busqueda del valor dentro del arreglo
bus=int(input("Ingrese el valor buscado: "))
print("La pocision del buscado sera: ")
for i in range(m):
    if valor[i]==bus:
        r=i
        print("La posicion del elemento es", r+1)
        break