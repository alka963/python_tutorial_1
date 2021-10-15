class Father:
    def m1(self):
        print('Parent Class')
class Mother:
    def m1(self):
        print('Mother Class')
class Child(Father,Mother):
    def m3(self):
        self.m1()
c = Child()
c.m3()
