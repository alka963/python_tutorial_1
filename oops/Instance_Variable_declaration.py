class demo:
    def __init__(self):
        self.emp_no = 101
    def m1(self):
        self.emp_name = 'Akash'
    @classmethod
    def m2(cls):
        ob.emp_dept = 'Mech'
    @staticmethod
    def m3():
        ob.emp_sal = 3000000
ob = demo()
ob.emp_pf = 20000
ob.m1()
ob.m2()
ob.m3()
print(ob.__dict__)
