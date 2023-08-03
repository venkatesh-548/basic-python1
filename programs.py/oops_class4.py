class Student(object):
    def __init__(self):
        self.sid=232
        self.sname="venky"
        self.smarks=473
        self.savg=0.0
    def processdata(self):
        self.savg=self.smarks/6
    def show(self):
        print("student id",self.sid)
        print("student name",self.sname)
        print("student marks",self.smarks)
        print("student average",self.savg)
S=Student()
S.processdata()
S.show()
