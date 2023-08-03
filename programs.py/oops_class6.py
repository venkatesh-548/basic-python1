class Student(object):
    def __init__(self,p=0,q=0,r=0):
        self.id=p
        self.name=q
        self.marks=r
    def showdata(self):
        print("id:",self.id)
        print("name:",self.name)
        print("marks:",self.marks)
n=int(input("enter noi of students:"))
i=1
while(i<=n):
    l=int(input("enter id:"))
    m=input("enter name:")
    s=int(input("enter marks:"))
    s=Student(l,m,s)
    s.showdata()
    print('______________________')
    i=i+1
