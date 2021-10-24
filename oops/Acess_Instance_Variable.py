class demo:
    def __init__(self):
        self.emp_no = 101
        print('Employee No is: ',self.emp_no)
    def m1(self):
        self.emp_name = 'Akash'
        print('Employee Name is: ',self.emp_name)
    @classmethod
    def m2(cls):
        ob.emp_dept = 'Mech'
        print('Employee Department is: ',ob.emp_dept)
    @staticmethod
    def m3():
        ob.emp_sal = 3000000
        print('Employee Salary is: ',ob.emp_sal)
ob = demo()
ob.emp_pf = 20000
print('Employee pf is: ',ob.emp_pf)
ob.m1()
ob.m2()
ob.m3()
print(ob.__dict__)
