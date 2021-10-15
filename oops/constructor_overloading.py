class Test:
    def __init__(self):
        print("Test Constructor")
class Demo(Test):
    def __init__(self):
        super().__init__()
        print('Demo Constructor')
Demo()