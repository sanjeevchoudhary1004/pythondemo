class x:
    def m1(self):
        print("in no param m1 of x")
    def m1(self,a):
        print("in one param m1 of x")
    def m1(self, a, b):
        print("in two param m1 of x")



x1 = x()
x1.m1(1000)