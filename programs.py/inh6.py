class Alpha():
    def __init__(self):
        self.val1=100
    def show(self):
        print(self.val1)
class Beta(Alpha):
    pass
B=Beta()
B.show()
