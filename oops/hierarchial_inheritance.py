class Father:
    def m1(self):
        print("merey pyare Papa....")
class Child1(Father):
    def m2(self):
        self.m1()
        print('First Child')
class Child2(Father):
    def m2(self):
        self.m1()
        print('Second Child')
c = Child2()
c.m2()
c.m2()