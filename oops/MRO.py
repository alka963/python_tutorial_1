class Father:
    def m1(self):
        print('Parent Class')
class Mother:
    def m1(self):
        print('Mother Class')
class Child(Father,Mother):
    def __init__(self):
        self.m1()
        super().__init__()
        print('Child Class')
c = Child()

