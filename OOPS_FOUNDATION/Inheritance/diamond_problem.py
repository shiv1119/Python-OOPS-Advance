class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("show")

class D(B, C):
    def show(self):
        return print("D")

d = D()
print(d.show)
print(D.__mro__)
