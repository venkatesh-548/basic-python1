class Emp():
    def setname(self,name):
        self.name=name
    def getname(self):
        return self.name
    def setid(self,id):
        self.id=id
    def getid(self):
        return self.id
    def setaddress(self,address):
        self.address=address
    def getaddress(self):
        return self.address
class Bank(Emp):
    def setacnum(self,acnum):
        self.acnum=acnum
    def getacnum(self):
        return self.acnum
b=Bank()
b.setname(input("enter name:"))
b.setid(int(input("enter id:")))
b.setaddress(input("enter address:"))
b.setacnum(int(input("enter acnum:")))
print("idnum:",b.getid())
print("name:",b.getname())
print("address:",b.getaddress())
print("acnum:",b.getacnum())
