class demo:
    emp_id = 10001
    def __init__(self):
        demo.emp_no = 101
    def m1(self):
        demo.emp_name = 'Akash'
    @classmethod
    def m2(cls):
        demo.emp_dept = 'Mech'
    @staticmethod
    def m3():
        demo.emp_sal = 3000000
ob = demo()
demo.emp_pf = 20000
ob.m1()
ob.m2()
ob.m3()
print(demo.__dict__)
