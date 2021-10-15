class Grand:
    def m1(self):
        print('Home')
class Parent(Grand):
    def m2(self):
        print('Money')
class Child(Parent):
    def process(self):
        self.m1()
        self.m2()
c = Child()
c.process()