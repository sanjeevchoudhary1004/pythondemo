class x:
    def __init__(self):
        print("in constructor of X")
    def display(self):
        print("Welcome")
    def __del__(self):
        print("in destructor of X")
x().display()
