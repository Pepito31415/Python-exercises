print("-----------------------------------------------------")
print("SUCURSALES DE UNA EMPRESA")
print("-----------------------------------------------------")

MONTO=[]

#entrada

print("Ingrese numeros de sucursales y años:_")
N=int(input("Numero de Sucursales: "))
M=int(input("Numero de años: "))

for i in range(M):
    MONTO.append([])

    for j in range(N):
        print("Ingrese ventas de la sucursal", j+1,"en el año",i+1)
        venta=int(input())
        MONTO[i].append(venta)

#proceso
print("\n SUCURSA CON MAS VENTAS: ")
print("-----------------------------------------------------")
MAX=0
for j in range(N):
    SUMA=0
    for i in range(M):
        SUMA=SUMA + MONTO[i][j]
    print("Numero de ventas de la sucursal", j+1,"es",SUMA)
    if SUMA>MAX:
        MAX=SUMA
        SUC=j+1 #se incrementa j, por conteo desde 0

print("sucursal que mas vendio:", SUC)
print("-----------------------------------------------------")
print("Promedio de ventas del año: ")
print("-----------------------------------------------------")
MAX =0
for i in range(M):
    SUMA=0

    for j in range(N):
        SUMA=SUMA+ MONTO[i][j]
        PROM=SUMA/N
        print("promedio de ventas del año", i+1,"es", PROM)

        if PROM>MAX:
            MAX=PROM
            ANIO=i+1

print("Año con mayor promedio ", ANIO)             