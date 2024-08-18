#Escribir un algritmo que calcule los numeros primos de 0 a 100 utilizando
#el llamado del metodo de la criba de eratostenes.
#Este metodo consiste en definir e inicializar con todos sus
# elementos a Ture un vector de 100 elementos de binarios e ir
#"tachando" (pasando a False) en pasadas sucesivas todos ños multi´ples dew los numeros primos (2,3,5,7)
#hasta solo obtener numeros primos:

print("-------------------------------------------------")
print("CRIBA DE ERATOTOSTENES.")
print("-------------------------------------------------")

#inicializar
B=100*[True]

N=[]
for i in range(1,100+1):
    N.append(i)

#proceso
B[0]=False

for i in range(1,99):
    for j in range(i+1,100):
        if N[j]%N[i]==0:
            B[j]=False

for i in range(100):
    if B[i]:
        print(N[i])