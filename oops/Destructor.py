import time
class Employee:
    def __init__(self):
        print('constructor')
    def __del__(self):
        print('Destructor')
employee = Employee()
time.sleep(5)
print('End of Application')