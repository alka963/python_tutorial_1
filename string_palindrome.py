str = input('enter string')
l = len(str)
b = str[-1::-1]
temp = str
if str == b:
    print('palindrome')
else:
    print('not palindrome')