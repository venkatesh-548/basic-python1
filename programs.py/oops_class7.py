class Testclass(object):
    def __init__(self):
        self.x=1
    def modify(self):
        self.x+=1
    def show(self):
        print(self.x)
T1=Testclass()
T2=Testclass()
T1.modify()
T1.show()
T2.modify()
T2.show()
