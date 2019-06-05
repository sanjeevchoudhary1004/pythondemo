class X:
    a = 1000
    def m1(self):
        print("in m1 of X")
class Y(X):
    b = 2000
    def __init__(self):
        self.c = 3000
    def m2(self):
        print("in m2 of Y")
print(Y.a)
print(Y.b)
Y1=Y()
print(Y1.c)
Y1.m1()
Y1.m2()

class Z:
    def __init__(self):
        print("in constructor of Z")
    def m1(self):
        print("in m1 of Z")
class M(Z):
    def m2(self):
        print("in m2 of M")
M1=M()
M1.m1()
M1.m2()
