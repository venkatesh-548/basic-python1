class Testclass(object):
    x=1
    @classmethod
    def modify(cls):
        cls.x+=1
    def show(cls):
        print(cls.x)
T1=Testclass()
T2=Testclass()
T1.modify()
T1.show()
T2.show()
