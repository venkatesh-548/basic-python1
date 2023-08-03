#finding instance using static variable
class Myclass():
    n=0
    def __init__(self):
        Myclass.n=Myclass.n+1
    @staticmethod
    def countobjects():
        print("tthe no of objects:",Myclass.n)
m1=Myclass()
m2=Myclass()
m3=Myclass()
Myclass.countobjects()
        
