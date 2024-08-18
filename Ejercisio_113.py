#Ejercisio 113: implementa un sistema para una tienda en linea. crea una clase
# base "discount" con metodos como "apply_discount()".
# -Luego , extiende esta clases como "PercentageDiscount" y "fixedAmauntDiscount" 
# sin modificar el codigo original.

#Aplicar e principio de abierto cerrado.

class Discount:
    def __init__(self, compra, costo):
        self.costo=costo
        self.compra=compra

    def apply_discount(self,compra, costo):
        print("-------------------------------------------")
        print(f"El precio de {compra} es de {costo}")
        return "-------------------------------------------"

class PercentageDiscount(Discount):
    def porcent_discount(self,compra,costo):
        if compra=="Sony":
            costo=costo-(costo/100*20)
            print("-------------------------------------------")
            print(f"su compra es de {costo}$")
            return "-------------------------------------------"
            
        elif costo > 120:
            costo=costo-(costo/100*20)
            print("-------------------------------------------")
            print(f"su compra es de {costo}$")
            return "-------------------------------------------"
        else:
            pass

class FixedAmauntDiscount(Discount):
    def fijo_descuento(self, compra, costo):
        if compra=="Sony" and costo>120:
            print("-------------------------------------------------")
            print("Su descuento fijo es de 40 porciento")
            return "-------------------------------------------"
        elif compra=="Sony" or costo>120:
            print("-------------------------------------------------")
            print("Su descuento fjo es de 20 porciento")
            return "-------------------------------------------"
        else:
            print("-------------------------------------------------")
            print("SU COMPRA no tiene descuenco")
            return "-------------------------------------------"

producto=input("Ingrese el producto:_ ")
print("--------------------------------------")
costo=int(input("Ingrese el costo:_ "))
print("--------------------------------------")

descuento=Discount(producto, costo)
d_fijo=FixedAmauntDiscount(producto, costo)
p_descuento=PercentageDiscount(producto, costo)

print(descuento.apply_discount(producto, costo))
print(p_descuento.porcent_discount(producto, costo))
print(d_fijo.fijo_descuento(producto, costo))