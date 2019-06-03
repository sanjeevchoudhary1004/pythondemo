class x:
    def __init__(self):
        print("in constructor of x")
    def __del__(self):
        print("in destructor of x")
    def display(self):
        print("Welcome")
x1 = x()
print(x1)
x2 = x1
print(x2)
x3 = x2
print(x3)
del x1
del x2
del x3
print(" ")
class y:
    def __init__(self):
        print("in constructor of y")
    def __del__(self):
        print("in destructor of y")
        print("Welcome")
y1 = y()
del y1
y()
