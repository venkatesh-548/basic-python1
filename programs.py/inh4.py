#single inheritance
class Emp():
    def setid(self,id):
        self.id=id
    def setname(self,name):
        self.name=name
    def setaddress(self,address):
        self.address=address
    def getid(self):
        return self.id
    def getname(self):
        return self.name
    def getaddress(self):
        return self.address
class Bank(Emp):
    def setacnum(self,acnum):
        self.acnum=acnum
    def getacnum(self):
        return self.acnum
B=Bank()
B.setid(540)
B.setname('venky')
B.setaddress("3-136,main road,Gdasam,Vizianagaram,AP")
B.setacnum(12635467786)
print("id:",B.getid())
print("name:",B.getname())
print("address:",B.getaddress())
print("Account Number:",B.getacnum())
