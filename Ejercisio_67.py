#Ejercisio 67: convertir Kilopascales (kPa) en presion psi, mmHg,y atm.

def conversion_kilopascales(kpa):
    psi=kpa/6.89475729
    mmhg= kpa*760/101.325
    atm= kpa/101.325

    return psi, mmhg, atm


kilopascales= float(input("Escribe la presion en kilopascales (kPa). "))
print(conversion_kilopascales(kilopascales))
