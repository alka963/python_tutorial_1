class Father:
    def m1(self):
        print('home')
class Mother:
    def m2(self):
        print('Money')
class Child(Father,Mother):
    def process(self):
        self.m1()
        self.m2()
c = Child()
c.process()