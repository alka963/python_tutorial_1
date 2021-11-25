import pickle
class Student:
    def __init__(self):
        self.sname = input('Enter a student Name: ')
        self.sroll = int(input('Enter roll no:'))
        self.course = input('Enter your course:')
    def __str__(self):
        return 'student Name :' + self.sname + ' \n' + "" + 'student rollno :' + str(self.sroll) + '\n' + "" + 'course :' + self.course
with open('Employee.dat', "rb") as f:
    s = pickle.load(f)
    print(s)