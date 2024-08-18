def sumar_dos():
    while True:
        a=input("Numero 1: ")
        b=input("Numero 2: ")
        try:
            resultado= int(a)+ int(b)
        except Exception as e:
            print("por favor introduzca un numero, no un texto")
            print(f"ERROR: {e}")
        else:
            break
        finally:
            print("Esto se ejecutara siempre")
    return resultado

print(sumar_dos())