class Base:
    def show(self):
        print("Base")

class A(Base):
    def show(self):
        print("A")
        super().show()

class B(A):
    def show(self):
        print("B")
        super().show()

class C(A):
    def show(self):
        print("C")
        super().show()

class D(B, C):
    def show(self):
        print("D")
        super().show()

d = D()
d.show()