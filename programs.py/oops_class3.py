class Employee(object):
    def __init__(self):
        self.eid=100
        self.ename="venky"
        self.esal=32000
        print("constructor executed")
    def show(self):
        print("emp id",self.eid)
        print("emp name",self.ename)
        print("emp salary",self.esal)
E=Employee()
E.show()
