#Ejercisio 78: realizar el pseudocodigo parar realizar dos matrizes.

print("---------------------------------------------------------------")
print("SUMA DE MATRIZES: ")
print("---------------------------------------------------------------")

A=[]
B=[]
C=[]

#Entradas:

print("ingrese dimencion de las matrizes, maximo 100")
S=int(input("Numeros de filas: "))
R=int(input("Numero de columnas: "))

#proceso

for i in range(S):
    A.append([])
    B.append([])
    C.append([])
    for j in range(R):
        A[i].append(int(input("A{}{}: ".format(i+1,j+1))))
        B[i].append(int(input("B{}{}: ".format(i+1,j+1))))
        C[i].append(A[i][j]+B[i][j])

print("\nSalida") 
print("---------------------------------------------------------------")
print(A)
print(B)
print(C)