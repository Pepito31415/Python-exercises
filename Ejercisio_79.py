#Dada una matriz cuadrada A, construlla un diagrama de flujo
#que permita determinar si dicha matriz es simetrica
#Se considera a una matriz simetrica si A (i,j)= A=(j,i) y esto se
#cumple para todos los elementos i,j de la matriz.

print("---------------------------------------------------------------")
print("Matriz simetrica/CALCULO: ")
print("---------------------------------------------------------------")


#lISTA
A=[]
#Entradas
N=int(input("Ingrese dimenciones de l angulo del arreglo:__ "))

#proceso
if 1<=N and N<=100:
    for i in range(N):
        A.append([])

        for j in range(N):
            elemento=input("A {}{}: ".format(i,j))
            A[i].append(int(elemento))

    BAND=True
    i=0
    while j<i-1 and BAND==True:

        j=0
        while j<i-1 and BAND==True:
            if A[i][j]==A[j][i]:
                j=j+1
            else:
                i=i+1
    if BAND:
        print("SI ES SIMETRICA")
    else:
        print("La dimension no es correcta")