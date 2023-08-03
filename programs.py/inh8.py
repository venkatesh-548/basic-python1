class Father():
    def show(self):
        print("my father give i cr property")
class Mother():
    def display(self):
        print("my mother color is fair")
class Child(Father,Mother):
    def output(self):
        print("my height is 6 feet")
C=Child()
C.show()
C.display()
C.output()
