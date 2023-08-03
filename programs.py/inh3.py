from inh1 import Emp

class Bank(Emp):
    def setacnum(self,acnum):
        self.acnum=acnum
    def getacnum(self):
        return self.acnum
B=Bank()
B.setid(548)
B.setname("nihal")
B.setaddress("gopalpatnam,vizag,AP")
B.setacnum(8721364783691237)
print("id number:",B.getid())
print("name:",B.getname())
print("address:",B.getaddress())
print("account number:",B.getacnum())
