class Student(object):
    def __init__(self,p,q,r):
        self.id=p
        self.name=q
        self.marks=r
    def showdata(self):
        print("id number:",self.id)
        print("name:",self.name)
        print("marks:",self.marks)
n=int(input("enter student id:"))
m=input("enter student name:")
s=int(input("enter student marks:"))
s1=Student(n,m,s)
s1.showdata()
n=int(input("enter student id:"))
m=input("enter student name:")
s=int(input("enter student marks:"))
s2=Student(n,m,s)
s2.showdata()       
        
