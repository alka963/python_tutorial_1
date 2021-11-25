import pickle
class Employee:
    def __init__(self, eno, ename, esal):
        self.eno = eno
        self.ename = ename
        self.esal = esal
    def __str__(self):
        return str(self.eno) + "" + self.ename + "" + str(self.esal)
with open('Employee.dat', "wb") as f:
    emp = Employee(101, 'san', 23000)
    pickle.dump(emp, f)
    print('save object')