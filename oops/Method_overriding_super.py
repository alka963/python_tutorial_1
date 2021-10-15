class Parent:
    def property(self):
        print('gold | cash | land')
    def marry(self):
        print("Mayawati...")
class Kunal(Parent):
    def marry(self):
        super().marry()
        print('Madhuri...')
k = Kunal()
k.property()
k.marry()