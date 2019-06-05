class X:
    a = 1000
    def m1(self):
        print("in m1 of x")

class Y(X):
    b = 2000
    def __init__(self):
        self.c = 3000

    def m2(self):
        print("in m2 of Y")
    def display(self):
        print(Y.a)
        print(Y.b)
        print(self.c)
        self.m1()
        self.m2()
Y1=Y()
Y1.display()