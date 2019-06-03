class Emp:
    """Emp App"""
    empcnt = 0
    def __init__(self,ename,eadd,eid,esal):
        self.ename = ename
        self.eadd = eadd
        self.eid = eid
        self.esal = esal
        Emp.empcnt = Emp.empcnt+1
    def __del__(self):
        Emp.empcnt = Emp.empcnt - 1

e1 = Emp("Scott","dallad","7788",3000.00)
e2 = Emp("Blake","mumbai","7902",3500.00)
e3 = Emp("smith","tokyo","7369",5000.00)

del e2
print("Total no of Employees are :",Emp.empcnt)

