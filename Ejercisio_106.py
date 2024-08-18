#Ejercisio: Usar los fundamentos del metodo MRO para definir y cordinar una herarquia de 9 clases.

class A:
    def hablar(self):
        print("Hola desde A")


class B(A):
    def hablar(self):
        print("Hola desde B")


class C(A):
    def hablar(self):
        print("Hola desde C")


class D(B,C):
    def hablar(self):
        print("Hola desde D")


class F(D):
    def hablar(self):
        print("Hola desde F")


class G(D):
    def hablar(self):
        print("Hola desde G")


class H(G,F):
    def hablar(self):
        print("Hola desde H")


class I(H):
    def hablar(self):
        print("Hola desde H")


class J(I,D):
    def hablar(self):
        print("Hola desde J")

j=J()

j.hablar()

print("\n",J.mro())
print("---------------------------------------------------------------------------")

class A:
    def hablar(self):
        print("Hola desde A")


class B(A):
    def hablar(self):
        print("Hola desde B")


class C(A):
    def hablar(self):
        print("Hola desde C")


class D(B,C):
    def hablar(self):
        print("Hola desde D")


class F(D):
    def hablar(self):
        print("Hola desde F")


class G(D):
    def hablar(self):
        print("Hola desde G")


class H(G,F):
    def hablar(self):
        print("Hola desde H")


class I(H):
    def hablar(self):
        print("Hola desde H")


class J(I,D):
    pass

j=J()

j.hablar()
print("\n",J.mro())
print("---------------------------------------------------------------------------")

class A:
    def hablar(self):
        print("Hola desde A")


class B(A):
    def hablar(self):
        print("Hola desde B")


class C(A):
    def hablar(self):
        print("Hola desde C")


class D(B,C):
    def hablar(self):
        print("Hola desde D")


class F(D):
    def hablar(self):
        print("Hola desde F")


class G(D):
    pass

class H(G,F):
    pass

class I(H):
    pass

class J(I,D):
    pass

j=J()

j.hablar()
print("\n",J.mro())
print("---------------------------------------------------------------------------")

class A:
    def hablar(self):
        print("Hola desde A")

class M:
    def hablar(self):
        print("Hola desde M")


class B(A):
    pass

class C(A):
    pass

class D(B,C,M):
    pass

class F(D):
    pass

class G(D):
    pass

class H(G,F):
    pass

class I(H):
    pass

class J(I,D):
    pass

j=J()

j.hablar()
print("\n",J.mro())
print("---------------------------------------------------------------------------")

class A:
    pass
class M:
    def hablar(self):
        print("Hola desde M")


class B(A):
    pass

class C(A):
    pass

class D(B,C,M):
    pass

class F(D):
    pass

class G(D):
    pass

class H(G,F):
    pass

class I(H):
    pass

class J(I,D):
    pass

j=J()

j.hablar()
print("\n",J.mro())
print("---------------------------------------------------------------------------")
