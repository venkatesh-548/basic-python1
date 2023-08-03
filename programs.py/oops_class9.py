#getter setter methods
class Getsmethod(object):
    def setnumber(self,num):
        self.number=num
    def getnumber(self):
        return(self.number)
    def setname(self,na):
        self.name=na
    def getname(self):
        return(self.name)
    def setmarks(self,mar):
        self.marks=mar
    def getmarks(self):
        return(self.marks)
obj=Getsmethod()
n=int(input("enter number:"))
obj.setnumber(n)
s=input("enter name:")
obj.setname(s)
x=int(input("enter marks:"))
obj.setmarks(x)
print("accessing of the data")
print(obj.getnumber())
print(obj.getname())
print(obj.getmarks())            
