class X:
    def m1(self):
        print("in m1 of x")
class Y(X):
    def m2(self):
        print("in m2 of Y")
print(X.__bases__)
print(Y.__bases__)
Y1=Y()
p = Y1.__hash__()
print(p)
Y1.m1()
Y1.m2()

class z:
    def m3(self):
        print("in m3 of z")
z1=z()
print(z1)
p=z1.__str__()
print(p)
z1.m3()