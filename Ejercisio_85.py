#Realizar un algoritmo que maneje un vector de enteros a traves
#de un menu con seis opciones.

print("-------------------------------------------------")
print("INTERACTUAR CON UN VECTOR A TRAVEZ DE OPCIONES.")
print("-------------------------------------------------")

v=100*[0]
i=0
#entradas
n=int(input("ingrese tamaño del vector:_ "))
opc=-1
while opc !=0:
    print("\n -------------------------------------------")
    print("ingrese 1 para añadir un elemento al vector.")
    print("-------------------------------------------------")
    print("Ingrese 2 para eliminar n elemente del vector")
    print("-------------------------------------------------")
    print("Ingrese 3 para listar el contenido de un vector")
    print("-------------------------------------------------")
    print("Ingrese 4 para contar las apariciones de Un numero en el vector")
    print("-------------------------------------------------")
    print("Ingrese 5 para calcular a media y el amximo de los elementos de un vector")
    print("-------------------------------------------------")
    print("ingrese 0 para terminar")
    print("-------------------------------------------------")

    opc=int(input("Ingrese opcion: "))
    if opc==1:
        if (i<n):
            v[i]=int(input("Ingrese Entero "))
            i=i+1
    elif opc==2:
        print("Ingrese el numero que desea eliminar ")
        num=int(input())
        if num>0:
            a=0
            for j in range(i):
                if v[j]==num:
                    a=j
                    break

    elif opc==3:
        if i>0:
            for j in range(i):
                print(v[j])
    elif opc==4:
        c=0
        num=int(input("ingrese numero para contar numero de apariciones :_ "))

        for j in range(i):
            if num==v[j]:
                c=c+1
        print("El numero de apariciones es: ",c)

    elif opc==5:
        max =v[0]
        ma=0
        for j in range(i):
            if max<v[j]:
                max=v[j]
            ma=ma+v[j]
        ma=ma/i
        print("el numero es:",max," y la media es:",ma)

    elif opc==0:
        print("FIN DE PROGRAMA")
        break