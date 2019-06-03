class x:
    def __init__(self):
        print("in constructor of x")
    def display(self):
        print("Welcome")
    def __del__(self):
        print("in destructor of x")
x1= x()
print(x1)
x2 = x1
print(x2)
x3 = x2
print(x3)
x1 =x()
print(x1)
x2 =x()
print(x2)
x3 = x()
print(x3)

