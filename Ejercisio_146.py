#Ejercisio 145: crear un juego  de piedra, papel, o tijeras.

import random 

lista=["roca","papel","tijeras"]

while True:
    computadora=random.choice(lista)
    jugador=None

    while jugador not in lista:
        jugador= input("roca, papel o tijera: ").lower()
    if jugador== computadora:
            print("computadora:", computadora)
            print("Jugador: ", jugador)
            print("EMPATE")
    elif jugador== "roca":
        if computadora == "papel":
                    print("computadora:", computadora)
                    print("Jugador: ", jugador)
                    print("perdiste")
        if computadora == "tijera":
                    print("computadora:", computadora)
                    print("Jugador: ", jugador)
                    print("ganaste")
    elif jugador== "papel":
        if computadora == "tijera":
                    print("computadora:", computadora)
                    print("Jugador: ", jugador)
                    print("perdiste")
        if computadora == "roca":
                    print("computadora:", computadora)
                    print("Jugador: ", jugador)
                    print("ganaste")
    elif jugador== "tijera":
        if computadora == "roca":
                    print("computadora:", computadora)
                    print("Jugador: ", jugador)
                    print("perdiste")
        if computadora == "papel":
                    print("computadora:", computadora)
                    print("Jugador: ", jugador)
                    print("ganaste")
                    
    jugar_de_nuevo=input("Quieres jugar de nuevo (si/no)").lower()
    
    if jugar_de_nuevo!='si':
        break

print("Adios")