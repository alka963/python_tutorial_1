import pickle
class Student:
    def __init__(self):
        self.sname = input('Enter student Name:')
        self.sroll = input('Enter student roll:')
        self.course = input('Enter a course:')
    def __str__(self):
        return self.sname + "" + str(self.sroll) + "" + self.course
with open("Employee.dat", 'wb') as f:
    emp = Student()
    pickle.dump(emp, f)
    print('save')