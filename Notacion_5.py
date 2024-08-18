#notacion 5: MRO(Metodo de Resolucion de Orden).

class A:
    def hablar(sefl):
        print("hola desde A")


class B(A):
    def hablar(sefl):
        print("hola desde B")


class C(A):
    def hablar(sefl):
        print("hola desde C")


class D(B,C):
    def hablar(sefl):
        print("hola desde D")

d=D()

d.hablar()

print("------------------------------------------------------------------")


class A:
    def hablar(sefl):
        print("hola desde A")


class B(A):
    pass

class C(A):
    def hablar(sefl):
        print("hola desde C")


class D(B,C):
    pass

d=D()

d.hablar()

print("------------------------------------------------------------------")


class A:
    def hablar(sefl):
        print("hola desde A")


class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

d=D()

d.hablar()
#La jerarquia presenteda aca se describe de esta forma D>B>C>A, ES DECIR...
# La herenca comienza desde a pero si no encuetra la herencia en las clases llamdas por el codigo
# va buscarlo por las clases de herencia mas cercana que tengan la funcion que el algortmo esta llamando.

print("------------------------------------------------------------------")


class A:
    def hablar(sefl):
        print("hola desde A")


class B(A):
    pass

class C(A):
    def hablar(sefl):
        print("hola desde C")


class D(B,C):
    pass

d=D()

d.hablar()

print("------------------------------------------------------------------")


class A:
    def hablar(sefl):
        print("hola desde A")

class F:
    def hablar(self):
        print("hablar desde F")

class B(A):
    pass

class C(F):
    def hablar(sefl):
        print("hola desde C")


class D(B,C):
    pass


d=D()

d.hablar()

print("------------------------------------------------------------------")


class A:
    pass

class F:
    def hablar(self):
        print("hablar desde F")

class B(A):
    pass

class C(F):
    pass

class D(B,C):
    pass


d=D()

d.hablar()

print("------------------------------------------------------------------")

class A:
    pass

class F:
    def hablar(self):
        print("hablar desde F")

class B(A):
    pass

class C(F):
    pass

class D(B,C):
    pass

print(D.mro())