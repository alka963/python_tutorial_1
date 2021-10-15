class Parent:
    def __init__(self):
        print('Parent')
class Child(Parent):
    def __init__(self):
        print('Child')
c = Child()