#Ejercisio 66: Calcular el indice de masa corporal (IMC).

def imc(estatura, peso):
    """
    Calcular el indice de masa corporal.
    """
    return peso/estatura **2

peso=float(input("escribe su peso (kg): "))
estatura= float(input("Escriba su estatura (m): "))

indice = imc(estatura, peso)

print("Su Imc es: ",indice)