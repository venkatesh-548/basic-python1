class Alpha():
    def __init__(self,k):
        self.val1=k
    def show(self):
        print("this is show metyhod in parent class")
    def display(self):
        print("this is display method in parent class")
class Beta(Alpha):
    def __init__(self,x,y):
        super(). __init__(y)
        self.val2=x
    def show(self):
        super().show()
        print("sum:",self.val1+self.val2)
B=Beta(10,30)
B.show()
B.display()
