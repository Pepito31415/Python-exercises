#Se tiene un vector, se pide ingresar 200 nombres de animales,
# luego se debe buscar el nombre de un animal que se ingrese por teclado 
# el algoritmo debe imprimir el nombre de los animales que se encuentran
# al lado de la posicion donde esta el animal
# buscando, tanto a la derecha como izquierda.

print("----------------------------------")
print("JUGANDO CON NOMBRES DE ANIMALES.")
print("----------------------------------")

animal=[]

print("Ingresar diimencion del array: ")
tam_array=int(input())

print("ingrese los nombres de los animales: ")
for x in range(tam_array):
    elemento=input("ingrese Animal{}: ".format(x+1))
    animal.append(elemento)

print("Ingrese anmal buscado: ")
nom=input()
print("El animal tiene como vecino a: ")
print("----------------------------------")
for x in range(tam_array):
    if animal[x]== nom:
        if x==0:
            print(animal[x+1])

        elif x ==tam_array-1:
            print(animal[x-1])

        else:
            print(animal[x-1])
            print(animal[x+1])