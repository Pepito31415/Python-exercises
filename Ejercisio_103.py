#Ejercisio 103: Generar n cantidad de numeros primos consecutivos.

def generar_primo():
    numero=2

    yield numero
    while True:
        temp=numero
        while True:
            temp +=1
            contador= 1
            contador_divisores=0

            while contador<= temp:
                if temp % contador ==0:
                    contador_divisores+=1

                if contador_divisores>2:
                    break

                contador+=1

            if contador_divisores==2:
                yield temp
                numero= temp

g= generar_primo()

primos=[next(g) for _ in range(5)]

print(primos)